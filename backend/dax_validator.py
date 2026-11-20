
import re
from backend.schema_retriever import load_schema, get_value


# ============================================================
# 1. BLOCKED DAX KEYWORDS
# ============================================================

BLOCKED_KEYWORDS = [
    "CREATE",
    "ALTER",
    "DROP",
    "DELETE",
    "INSERT",
    "UPDATE",
    "TRUNCATE",
    "MERGE",
    "EXEC",
    "EXECUTE",
    "OPENROWSET",
    "OPENDATASOURCE",
    "BACKUP",
    "RESTORE",
]


# ============================================================
# 2. REGEX PATTERNS
# ============================================================

COLUMN_PATTERN = r"'([^']+)'\s*\[([^\]]+)\]"

BRACKET_REFERENCE_PATTERN = r"\[([^\]]+)\]"


# ============================================================
# 3. CLEAN DAX
# ============================================================

def clean_dax(dax):
    """
    Remove comments and string literals for structural checks.
    Preserve quoted table and column references.
    """

    # Remove block comments
    dax = re.sub(
        r"/\*.*?\*/",
        "",
        dax,
        flags=re.DOTALL
    )

    # Remove single-line comments
    dax = re.sub(
        r"--[^\n]*",
        "",
        dax
    )

    # Remove double-quoted string literals
    # Preserve double-quoted strings separately for alias detection.
    dax = re.sub(
        r'"(?:[^"]|"")*"',
        '""',
        dax
    )

    return dax.strip()


# ============================================================
# 4. NORMALIZE METADATA
# ============================================================

def get_metadata_sets(schema=None):

    # Load complete live metadata, not question-specific metadata.
    full_schema = load_schema()

    measures = set()
    columns = set()
    tables = set()

    # --------------------------------
    # 1. Get ALL model columns
    # --------------------------------

    for _, row in full_schema["columns"].iterrows():

        name = get_value(row, "Name")
        table = get_value(row, "Table")

        if name and table:

            columns.add((
                table.strip().lower(),
                name.strip().lower()
            ))

            tables.add(table.strip().lower())

    # --------------------------------
    # 2. Get ALL model measures
    # --------------------------------

    for _, row in full_schema["measures"].iterrows():

        name = get_value(row, "Name")
        table = get_value(row, "Table")

        if name:
            measures.add(name.strip().lower())

        if table:
            tables.add(table.strip().lower())

    return measures, columns, tables


# ============================================================
# 5. MANDATORY AP108 FILTER VALIDATION
# ============================================================

def validate_mandatory_base_filters(dax):

    errors = []

    normalized = re.sub(r"\s+", "", dax).lower()

    ambulance_filter = (
        "'err'[ambulance/feeder vehicle]="
        '"ambulance"'
    )

    backup_filter = (
        "'err'[ambulance base location]<>"
        '"backup"'
    )

    # Normalize expected expressions too
    ambulance_filter = re.sub(
        r"\s+", "", ambulance_filter
    ).lower()

    backup_filter = re.sub(
        r"\s+", "", backup_filter
    ).lower()

    if ambulance_filter not in normalized:
        errors.append(
            'Missing mandatory filter: '
            '\'ERR\'[Ambulance/Feeder vehicle] = "Ambulance"'
        )

    if backup_filter not in normalized:
        errors.append(
            'Missing mandatory filter: '
            '\'ERR\'[Ambulance Base Location] <> "Backup"'
        )

    return errors


# ============================================================
# 6. VALIDATE DAX
# ============================================================

def validate_dax(dax, schema):

    errors = []
    warnings = []

    # --------------------------------------------------------
    # A. Basic input validation
    # --------------------------------------------------------

    if not isinstance(dax, str) or not dax.strip():

        return {
            "valid": False,
            "errors": ["DAX query is empty."],
            "warnings": warnings
        }

    original_dax = dax.strip()

    clean_query = clean_dax(original_dax)

    # --------------------------------------------------------
    # B. Query structure
    # --------------------------------------------------------

    if not re.match(
        r"^EVALUATE\b",
        clean_query,
        re.IGNORECASE
    ):

        errors.append(
            "Query must begin with EVALUATE."
        )

    if ";" in clean_query:

        errors.append(
            "Multiple statements or semicolons are not allowed."
        )

    # --------------------------------------------------------
    # C. Block unsafe keywords
    # --------------------------------------------------------

    for keyword in BLOCKED_KEYWORDS:

        if re.search(
            rf"\b{keyword}\b",
            clean_query,
            re.IGNORECASE
        ):

            errors.append(
                f"Blocked keyword detected: {keyword}"
            )

    # --------------------------------------------------------
    # D. Load approved metadata
    # --------------------------------------------------------

    measures, columns, tables = get_metadata_sets(schema)

    # --------------------------------------------------------
    # E. Validate table references
    # --------------------------------------------------------

    referenced_tables = set(
        re.findall(
            r"'([^']+)'",
            clean_query
        )
    )

    for table in referenced_tables:

        if table.strip().lower() not in tables:

            errors.append(
                f"Unknown table reference: '{table}'"
            )

    # --------------------------------------------------------
    # F. Validate column references
    # --------------------------------------------------------

    referenced_columns = re.findall(
        COLUMN_PATTERN,
        clean_query
    )

    for table, column in referenced_columns:

        normalized_reference = (
            table.strip().lower(),
            column.strip().lower()
        )

        if normalized_reference not in columns:

            errors.append(
                f"Unknown column reference: "
                f"'{table}'[{column}]"
            )

    # --------------------------------------------------------
    # G. Validate measure references
    # --------------------------------------------------------

    # Remove fully qualified column references first.
    query_without_columns = re.sub(
        COLUMN_PATTERN,
        "",
        clean_query
    )

    # Capture output aliases from original DAX.
    aliases = {
        alias.strip().lower()
        for alias in re.findall(
            r'"((?:[^"]|"")*)"\s*,',
            original_dax
        )
    }

    # Remaining bracket references may be measures
    # or output aliases such as [Completed Cases].
    measure_references = set(
        re.findall(
            BRACKET_REFERENCE_PATTERN,
            query_without_columns
        )
    )

    for measure in measure_references:

        normalized_measure = measure.strip().lower()

        if (
            normalized_measure not in measures
            and normalized_measure not in aliases
        ):

            errors.append(
                f"Unknown measure or column reference: [{measure}]"
            )

    # --------------------------------------------------------
    # H. Mandatory AP108 filters
    # --------------------------------------------------------

    base_filter_errors = validate_mandatory_base_filters(
        original_dax
    )

    errors.extend(base_filter_errors)

    # --------------------------------------------------------
    # I. Final validation result
    # --------------------------------------------------------

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }
