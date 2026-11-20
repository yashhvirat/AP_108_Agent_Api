
import re


# DAX statements and functions that must never be accepted.
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


def clean_dax(dax):
    """Remove comments and string literals for structural checks."""

    # Remove single-line comments
    dax = re.sub(r"--[^\n]*", "", dax)

    # Remove block comments
    dax = re.sub(r"/\*.*?\*/", "", dax, flags=re.DOTALL)

    # Remove double-quoted string literals
    dax = re.sub(r'"(?:[^"]|"")*"', '""', dax)

    return dax.strip()


def get_metadata_sets(schema):

    measures = {
        item["name"].strip()
        for item in schema.get("measures", [])
        if item.get("name")
    }

    columns = {
        (item["table"].strip(), item["name"].strip())
        for item in schema.get("columns", [])
        if item.get("table") and item.get("name")
    }

    tables = set(schema.get("relevant_tables", []))

    # Include tables discovered from the retrieved columns/measures
    tables.update(table for table, _ in columns)

    tables.update(
        item["table"].strip()
        for item in schema.get("measures", [])
        if item.get("table")
    )

    return measures, columns, tables

def validate_mandatory_base_filters(dax):

    errors = []

    normalized = re.sub(r"\s+", "", dax).lower()

    ambulance_filter = (
        """'err'[ambulance/feeder vehicle]="ambulance" """
        .replace(" ", "")
    )

    backup_filter = (
        """'err'[ambulance base location]<>"backup" """
        .replace(" ", "")
    )

    if ambulance_filter not in normalized:
        errors.append(
            'Missing mandatory filter: '
            "'ERR'[Ambulance/Feeder vehicle] = \"Ambulance\""
        )

    if backup_filter not in normalized:
        errors.append(
            'Missing mandatory filter: '
            "'ERR'[Ambulance Base Location] <> \"Backup\""
        )

    return errors


def validate_dax(dax, schema):

    errors = []
    warnings = []

    if not isinstance(dax, str) or not dax.strip():
        return {
            "valid": False,
            "errors": ["DAX query is empty."],
            "warnings": warnings
        }

    original_dax = dax.strip()
    clean_query = clean_dax(original_dax)

    # --------------------------------
    # 1. Basic query structure
    # --------------------------------

    if not re.match(r"^EVALUATE\b", clean_query, re.IGNORECASE):
        errors.append("Query must begin with EVALUATE.")

    # Only one DAX query is allowed.
    if ";" in clean_query:
        errors.append("Multiple statements or semicolons are not allowed.")

    # --------------------------------
    # 2. Block unsafe keywords
    # --------------------------------

    for keyword in BLOCKED_KEYWORDS:

        if re.search(
            rf"\b{keyword}\b",
            clean_query,
            re.IGNORECASE
        ):
            errors.append(
                f"Blocked keyword detected: {keyword}"
            )

    # --------------------------------
    # 3. Load approved metadata
    # --------------------------------

    measures, columns, tables = get_metadata_sets(schema)

    # --------------------------------
    # 4. Validate table references
    # --------------------------------

    referenced_tables = set(
        re.findall(r"'([^']+)'", clean_query)
    )

    for table in referenced_tables:

        if table not in tables:
            errors.append(
                f"Unknown table reference: '{table}'"
            )

    # --------------------------------
    # 5. Validate column references
    # --------------------------------

    column_pattern = r"'([^']+)'\s*\[([^\]]+)\]"

    referenced_columns = re.findall(
        column_pattern,
        clean_query
    )

    for table, column in referenced_columns:

        if (table, column) not in columns:
            errors.append(
                f"Unknown column reference: "
                f"'{table}'[{column}]"
            )

    # --------------------------------
    # 6. Validate measure references
    # --------------------------------

    # Remove fully qualified column references first.
    query_without_columns = re.sub(
        column_pattern,
        "",
        clean_query
    )

    # Collect aliases such as:
    # "Dispatches", [Dispatches]
    aliases = set(
        re.findall(
            r'"([^"]+)"\s*,',
            original_dax
        )
    )

    measure_references = set(
        re.findall(
            r"\[([^\]]+)\]",
            query_without_columns
        )
    )

    for measure in measure_references:

        if measure not in measures and measure not in aliases:
            errors.append(
                f"Unknown measure or column reference: [{measure}]"
            )

    # Mandatory AP108 base-filter validation
    base_filter_errors = validate_mandatory_base_filters(dax)

    errors.extend(base_filter_errors)

    # --------------------------------
    # 7. Final result
    # --------------------------------

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }
