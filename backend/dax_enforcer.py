
import re

from backend.schema_retriever import load_schema, get_value


# ============================================================
# AP108 MANDATORY GLOBAL FILTERS
# ============================================================

MANDATORY_FILTERS = [
    {
        "table": "ERR",
        "column": "Ambulance/Feeder vehicle",
        "operator": "=",
        "value": '"Ambulance"',
        "expression": (
            '\'ERR\'[Ambulance/Feeder vehicle] = "Ambulance"'
        )
    },
    {
        "table": "ERR",
        "column": "Ambulance Base Location",
        "operator": "<>",
        "value": '"Backup"',
        "expression": (
            '\'ERR\'[Ambulance Base Location] <> "Backup"'
        )
    }
]


# ============================================================
# PARENTHESES AND ARGUMENT PARSING
# ============================================================

def find_matching_parenthesis(text, open_index):
    """
    Find the closing parenthesis corresponding to open_index.
    Handles parentheses inside quoted strings.
    """

    depth = 0
    in_string = False
    i = open_index

    while i < len(text):

        char = text[i]

        if char == '"':
            if in_string and i + 1 < len(text) and text[i + 1] == '"':
                i += 2
                continue

            in_string = not in_string

        elif not in_string:

            if char == "(":
                depth += 1

            elif char == ")":
                depth -= 1

                if depth == 0:
                    return i

        i += 1

    return None


def split_top_level_arguments(text):
    """
    Split function arguments by commas at the current level only.
    """

    arguments = []

    start = 0
    depth = 0
    in_string = False
    in_bracket = False
    in_table = False

    i = 0

    while i < len(text):

        char = text[i]

        if char == '"':
            if in_string and i + 1 < len(text) and text[i + 1] == '"':
                i += 2
                continue

            in_string = not in_string

        elif not in_string:

            if char == "'" and not in_bracket:
                in_table = not in_table

            elif char == "[" and not in_table:
                in_bracket = True

            elif char == "]" and not in_table:
                in_bracket = False

            elif not in_bracket and not in_table:

                if char == "(":
                    depth += 1

                elif char == ")":
                    depth -= 1

                elif char == "," and depth == 0:
                    arguments.append(text[start:i].strip())
                    start = i + 1

        i += 1

    final_argument = text[start:].strip()

    if final_argument:
        arguments.append(final_argument)

    return arguments


# ============================================================
# METADATA VALIDATION
# ============================================================

def verify_mandatory_columns():

    full_schema = load_schema()

    available_columns = set()

    for _, row in full_schema["columns"].iterrows():

        table = get_value(row, "Table")
        column = get_value(row, "Name")

        if table and column:
            available_columns.add(
                (table.strip().lower(), column.strip().lower())
            )

    missing = []

    for item in MANDATORY_FILTERS:

        key = (
            item["table"].lower(),
            item["column"].lower()
        )

        if key not in available_columns:
            missing.append(
                f"'{item['table']}'[{item['column']}]"
            )

    if missing:
        raise ValueError(
            "Mandatory AP108 filter columns missing from "
            "live metadata: " + ", ".join(missing)
        )

    return True


# ============================================================
# FILTER DETECTION
# ============================================================

def normalize_expression(expression):

    return re.sub(
        r"\s+",
        " ",
        expression.strip()
    ).lower()



def argument_has_filter(argument, item, allow_direct=False):
    expected = normalize_expression(item["expression"])

    # Check whether this argument is a FILTER('ERR', condition) expression.
    filter_calls = find_function_calls(argument, "FILTER")

    for call in filter_calls:
        filter_arguments = split_top_level_arguments(
            argument[call["open"] + 1:call["close"]]
        )

        if len(filter_arguments) < 2:
            continue

        source_table = normalize_expression(filter_arguments[0])

        if source_table != "'err'":
            continue

        condition = normalize_expression(filter_arguments[1])

        if expected in condition:
            return True

    # CALCULATETABLE also supports direct Boolean filter arguments.
    if allow_direct:
        return normalize_expression(argument) == expected

    return False


def get_missing_filters(dax):
    missing = []

    summarize_calls = find_function_calls(dax, "SUMMARIZECOLUMNS")
    calculate_calls = find_function_calls(dax, "CALCULATETABLE")

    if len(summarize_calls) == 1:
        call = summarize_calls[0]

        arguments = split_top_level_arguments(
            dax[call["open"] + 1:call["close"]]
        )

        first_output_index = None

        for index, argument in enumerate(arguments):
            if argument.strip().startswith('"'):
                first_output_index = index
                break

        if first_output_index is None:
            raise ValueError(
                "Could not identify SUMMARIZECOLUMNS output expressions."
            )

        # Only inspect filter-table arguments before output expressions.
        filter_arguments = arguments[:first_output_index]

        for item in MANDATORY_FILTERS:
            found = any(
                argument_has_filter(argument, item)
                for argument in filter_arguments
            )

            if not found:
                missing.append(item)

    elif len(calculate_calls) == 1:
        call = calculate_calls[0]

        arguments = split_top_level_arguments(
            dax[call["open"] + 1:call["close"]]
        )

        if not arguments:
            raise ValueError("CALCULATETABLE has no arguments.")

        # Only inspect filter arguments after ROW(...).
        filter_arguments = arguments[1:]

        for item in MANDATORY_FILTERS:
            found = any(
                argument_has_filter(
                    argument,
                    item,
                    allow_direct=True
                )
                for argument in filter_arguments
            )

            if not found:
                missing.append(item)

    else:
        raise ValueError(
            "Expected exactly one supported SUMMARIZECOLUMNS "
            "or CALCULATETABLE query structure."
        )

    return missing


# ============================================================
# FUNCTION CALL DETECTION
# ============================================================

def find_function_calls(dax, function_name):
    """
    Locate function calls and their matching parentheses.
    """

    pattern = re.compile(
        rf"\b{re.escape(function_name)}\s*\(",
        flags=re.IGNORECASE
    )

    results = []

    for match in pattern.finditer(dax):

        open_index = dax.find("(", match.start())

        close_index = find_matching_parenthesis(
            dax,
            open_index
        )

        if close_index is None:
            raise ValueError(
                f"Unclosed {function_name} function."
            )

        results.append({
            "start": match.start(),
            "open": open_index,
            "close": close_index
        })

    return results


# ============================================================
# SUMMARIZECOLUMNS ENFORCEMENT
# ============================================================

def enforce_summarizecolumns(dax, missing_filters):

    calls = find_function_calls(
        dax,
        "SUMMARIZECOLUMNS"
    )

    if len(calls) != 1:
        raise ValueError(
            "Expected exactly one SUMMARIZECOLUMNS call. "
            "Unsupported or ambiguous query structure."
        )

    call = calls[0]

    arguments_text = dax[
        call["open"] + 1:call["close"]
    ]

    arguments = split_top_level_arguments(
        arguments_text
    )

    if not arguments:
        raise ValueError(
            "SUMMARIZECOLUMNS contains no arguments."
        )

    # Find the first output name/expression pair.
    # Output names are DAX string literals.

    first_output_index = None

    for index, argument in enumerate(arguments):

        if argument.strip().startswith('"'):
            first_output_index = index
            break

    if first_output_index is None:
        raise ValueError(
            "Could not identify output expressions in "
            "SUMMARIZECOLUMNS."
        )

    # Insert mandatory filter-table expressions
    # before output name/expression pairs.

    new_filters = []

    for item in missing_filters:

        expression = item["expression"]

        new_filters.append(
            f"FILTER('ERR', {expression})"
        )

    arguments[first_output_index:first_output_index] = new_filters

    updated_arguments = ",\n        ".join(arguments)

    updated_call = (
        "SUMMARIZECOLUMNS(\n        "
        + updated_arguments
        + "\n    )"
    )

    return (
        dax[:call["start"]]
        + updated_call
        + dax[call["close"] + 1:]
    )


# ============================================================
# CALCULATETABLE ENFORCEMENT
# ============================================================

def enforce_calculatetable(dax, missing_filters):

    calls = find_function_calls(
        dax,
        "CALCULATETABLE"
    )

    if len(calls) != 1:
        raise ValueError(
            "Expected exactly one CALCULATETABLE call. "
            "Unsupported or ambiguous query structure."
        )

    call = calls[0]

    arguments_text = dax[
        call["open"] + 1:call["close"]
    ]

    arguments = split_top_level_arguments(
        arguments_text
    )

    if not arguments:
        raise ValueError(
            "CALCULATETABLE contains no arguments."
        )

    first_argument = arguments[0].strip()

    if not re.match(
        r"^ROW\s*\(",
        first_argument,
        flags=re.IGNORECASE
    ):
        raise ValueError(
            "Ungrouped query must use "
            "CALCULATETABLE with ROW."
        )

    # Add missing mandatory filters as independent
    # CALCULATETABLE filter arguments.

    for item in missing_filters:

        arguments.append(
            item["expression"]
        )

    updated_arguments = ",\n        ".join(arguments)

    updated_call = (
        "CALCULATETABLE(\n        "
        + updated_arguments
        + "\n    )"
    )

    return (
        dax[:call["start"]]
        + updated_call
        + dax[call["close"] + 1:]
    )


# ============================================================
# MAIN ENFORCER
# ============================================================

def enforce_dax(dax, schema=None):

    try:

        if not isinstance(dax, str) or not dax.strip():
            raise ValueError(
                "DAX query is empty."
            )

        # 1. Verify mandatory columns against complete
        # live semantic model metadata.

        verify_mandatory_columns()

        # 2. Check query format.

        cleaned_dax = dax.strip()

        if not re.match(
            r"^EVALUATE\b",
            cleaned_dax,
            flags=re.IGNORECASE
        ):
            raise ValueError(
                "DAX query must begin with EVALUATE."
            )

        # 3. Find mandatory filters that are missing.

        missing_filters = get_missing_filters(
            cleaned_dax
        )

        # 4. If all filters are already present,
        # return the original query unchanged.

        if not missing_filters:

            return {
                "valid": True,
                "dax": cleaned_dax,
                "added_filters": [],
                "message": "All mandatory AP108 filters are present."
            }

        # 5. Detect supported query structures.

        summarize_calls = find_function_calls(
            cleaned_dax,
            "SUMMARIZECOLUMNS"
        )

        if summarize_calls:

            updated_dax = enforce_summarizecolumns(
                cleaned_dax,
                missing_filters
            )

        else:

            calculate_calls = find_function_calls(
                cleaned_dax,
                "CALCULATETABLE"
            )

            if calculate_calls:

                updated_dax = enforce_calculatetable(
                    cleaned_dax,
                    missing_filters
                )

            else:

                raise ValueError(
                    "Unsupported DAX structure. "
                    "Expected SUMMARIZECOLUMNS or "
                    "CALCULATETABLE(ROW(...))."
                )

        # 6. Verify that both filters are now present.

        remaining_filters = get_missing_filters(
            updated_dax
        )

        if remaining_filters:
            raise ValueError(
                "Mandatory AP108 filters could not be "
                "successfully enforced."
            )

        return {
            "valid": True,
            "dax": updated_dax,
            "added_filters": [
                item["expression"]
                for item in missing_filters
            ],
            "message": "Mandatory AP108 filters enforced successfully."
        }

    except Exception as error:

        return {
            "valid": False,
            "dax": None,
            "added_filters": [],
            "errors": [str(error)]
        }
