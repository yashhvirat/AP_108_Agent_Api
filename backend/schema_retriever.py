
import re
from functools import lru_cache

from backend.metadata import (
    get_tables,
    get_columns,
    get_measures,
    get_relationships
)


# Business terminology used in AP108
ALIASES = {
    "dispatches": [
        "dispatch",
        "ambulance dispatch",
        "ambulance dispatches",
        "assigned cases"
    ],
    "district": [
        "districts",
        "district final"
    ],
    "base location": [
        "base locations",
        "ambulance base location",
        "segments"
    ],
    "vehicle": [
        "vehicles",
        "vehicle number",
        "vehicle id"
    ],
    "date": [
        "dates",
        "call date",
        "event date"
    ]
}


# Extract qualified column references from DAX expressions.
COLUMN_REFERENCE_PATTERN = re.compile(
    r"'([^']+)'\s*\[([^\]]+)\]"
)


def normalize(text):
    text = str(text or "").lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)

    words = text.split()

    words = [
        word[:-1] if len(word) > 3 and word.endswith("s")
        else word
        for word in words
    ]

    return " ".join(words)


def get_value(row, field):

    value = row.get(f"[{field}]", "")

    if value is None:
        return ""

    if str(value).lower() == "nan":
        return ""

    return str(value).strip()


def is_noise_column(name):

    name = normalize(name)

    noise_terms = [
        "rownumber",
        "availability",
        "sort",
        "caller"
    ]

    return any(term in name for term in noise_terms)


@lru_cache(maxsize=1)
def load_schema():

    return {
        "tables": get_tables(),
        "columns": get_columns(),
        "measures": get_measures(),
        "relationships": get_relationships()
    }


def calculate_score(question, name, description=""):

    q = normalize(question)
    n = normalize(name)
    d = normalize(description)

    score = 0

    if n and n in q:
        score += 15

    q_words = set(q.split())
    n_words = set(n.split())

    score += len(q_words.intersection(n_words)) * 3

    d_words = set(d.split())
    score += len(q_words.intersection(d_words))

    for key, aliases in ALIASES.items():

        if normalize(key) in q or any(
            normalize(alias) in q for alias in aliases
        ):

            if n == normalize(key):
                score += 20

            if any(
                normalize(alias) in n
                for alias in aliases
            ):
                score += 15

    return score


def extract_measure_columns(expression):

    if not expression:
        return set()

    return {
        (table.strip().lower(), column.strip().lower())
        for table, column in COLUMN_REFERENCE_PATTERN.findall(
            str(expression)
        )
    }


def retrieve_schema(question, top_measures=15, top_columns=30, plan=None):

    schema = load_schema()

    # --------------------------------
    # 1. Find relevant measures
    # --------------------------------

    measure_results = []

    for _, row in schema["measures"].iterrows():

        name = get_value(row, "Name")
        table = get_value(row, "Table")
        description = get_value(row, "Description")
        expression = get_value(row, "Expression")

        score = calculate_score(
            question,
            name,
            description
        )

        if score > 0:

            measure_results.append({
                "name": name,
                "table": table,
                "description": description,
                "expression": expression,
                "score": score
            })

    measure_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    measure_results = measure_results[:top_measures]

    # --------------------------------
    # 2. Identify columns used by measures
    # --------------------------------

    measure_columns = set()

    relevant_tables = set()

    for measure in measure_results:

        if measure["table"]:
            relevant_tables.add(measure["table"])

        measure_columns.update(
            extract_measure_columns(measure["expression"])
        )

    # --------------------------------
    # 3. Identify question-relevant columns
    # --------------------------------

    q = normalize(question)

    # --------------------------------
    # Planner-requested grouping dimensions
    # --------------------------------

    requested_dimensions = set()

    if plan:
        for dimension in plan.get("group_by", []):
            requested_dimensions.add(normalize(dimension))

    date_requested = (
        any(month in q.split() for month in [
            "january", "february", "march", "april",
            "may", "june", "july", "august",
            "september", "october", "november", "december"
        ])
        or bool(re.search(r"\b20\d{2}\b", q))
        or any(
            word in q.split()
            for word in ["date", "month", "year", "week", "quarter"]
        )
    )

    column_candidates = []

    for _, row in schema["columns"].iterrows():

        name = get_value(row, "Name")
        table = get_value(row, "Table")
        data_type = get_value(row, "DataType")

        if not name or not table:
            continue

        if is_noise_column(name):
            continue

        score = calculate_score(question, name)

        normalized_name = normalize(name)
        normalized_type = normalize(data_type)

                # Exact planner-requested dimensions get priority.
        is_grouping_column = (
            normalized_name in requested_dimensions
        )

        if is_grouping_column:
            score += 100

        # Date-related columns are included when
        # the question contains a date/time requirement.
        if date_requested and (
            "date" in normalized_name
            or "time" in normalized_name
            or "date" in normalized_type
        ):
            score += 25

        # Exact column references from selected measures
        # are always retained.
        is_measure_column = (
            table.lower(),
            name.lower()
        ) in measure_columns

        if score > 0 or is_measure_column or is_grouping_column:

            column_candidates.append({
                "name": name,
                "table": table,
                "data_type": data_type,
                "score": score,
                "measure_reference": is_measure_column,
                "grouping_column": is_grouping_column
            })

            relevant_tables.add(table)

    # --------------------------------
    # 4. Build relevant column list
    # --------------------------------

    grouping_columns = [
        item for item in column_candidates
        if item.get("grouping_column", False)
    ]

    measure_reference_columns = [
        item for item in column_candidates
        if item["measure_reference"]
        and item not in grouping_columns
    ]

    other_columns = [
        item for item in column_candidates
        if not item["measure_reference"]
        and not item.get("grouping_column", False)
    ]

    other_columns.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Grouping columns and measure dependencies
    # are always retained, even beyond top_columns.

    priority_columns = (
        grouping_columns +
        measure_reference_columns
    )

    remaining_slots = max(
        0,
        top_columns - len(priority_columns)
    )

    column_results = (
        priority_columns +
        other_columns[:remaining_slots]
    )

    # --------------------------------
    # 5. Select relevant relationships
    # --------------------------------

    relationship_results = []

    for _, row in schema["relationships"].iterrows():

        from_table = get_value(row, "FromTable")
        to_table = get_value(row, "ToTable")
        is_active = get_value(row, "IsActive")

        if is_active.lower() != "true":
            continue

        if (
            from_table in relevant_tables
            and to_table in relevant_tables
        ):
            relationship_results.append(row.to_dict())

    return {
        "measures": measure_results,
        "columns": column_results,
        "relationships": relationship_results,
        "relevant_tables": sorted(relevant_tables)
    }
