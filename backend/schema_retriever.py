
import re
from functools import lru_cache

from metadata import (
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

def is_noise_column(name):

    name = normalize(name)

    noise_terms = [
        "rownumber",
        "availability",
        "sort",
        "caller"
    ]

    return any(term in name for term in noise_terms)


def normalize(text):

    text = str(text or "").lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)

    words = text.split()

    # Basic singular/plural normalization
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

    # Exact phrase match
    if n and n in q:
        score += 15

    # Word matching
    q_words = set(q.split())
    n_words = set(n.split())

    score += len(q_words.intersection(n_words)) * 3

    # Description matching
    d_words = set(d.split())
    score += len(q_words.intersection(d_words))

    # Alias matching
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


def retrieve_schema(question, top_measures=15, top_columns=30):

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
    # 2. Identify requested dimensions
    # --------------------------------

    q = normalize(question)

    requested_tables = set()

    # District dimension
    if "district" in q.split():
        requested_tables.add("Districts & Regions")

    # Region dimension
    if "region" in q.split():
        requested_tables.add("Districts & Regions")

    # Vehicle dimension
    if "vehicle" in q.split():
        requested_tables.add("Vehicles Master Database")

    # Base location dimension
    if "base location" in q:
        requested_tables.add("Segments")

    # Calendar detection, including month names and years
    month_names = [
        "january", "february", "march", "april",
        "may", "june", "july", "august",
        "september", "october", "november", "december"
    ]

    date_requested = (
        any(month in q for month in month_names)
        or bool(re.search(r"\b20\d{2}\b", q))
        or any(x in q.split() for x in ["date", "month", "year", "week"])
    )

    if date_requested:
        requested_tables.add("Calender")

    # --------------------------------
    # 3. Select relevant columns
    # --------------------------------

    relevant_tables = {
        item["table"] for item in measure_results
    }

    relevant_tables.update(requested_tables)

    column_results = []

    for _, row in schema["columns"].iterrows():

        name = get_value(row, "Name")
        table = get_value(row, "Table")
        data_type = get_value(row, "DataType")

        if table not in relevant_tables:
            continue

        # Remove unnecessary technical/helper columns
        if is_noise_column(name):
            continue

        score = calculate_score(question, name)

        if table in requested_tables:
            score += 20

        if score > 0 or table in requested_tables:
            column_results.append({
                "name": name,
                "table": table,
                "data_type": data_type,
                "score": score
            })

    column_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # --------------------------------
    # 4. Select relevant relationships
    # --------------------------------

    relationship_results = []

    for _, row in schema["relationships"].iterrows():

        from_table = get_value(row, "FromTable")
        to_table = get_value(row, "ToTable")
        is_active = get_value(row, "IsActive")

        if is_active.lower() != "true":
            continue

        # Keep only relationships connecting
        # the metric's fact table to requested dimensions.
        if (
            from_table in relevant_tables
            and to_table in relevant_tables
        ):
            relationship_results.append(row.to_dict())

        elif (
            to_table in relevant_tables
            and from_table in relevant_tables
        ):
            relationship_results.append(row.to_dict())

    return {
        "measures": measure_results,
        "columns": column_results[:top_columns],
        "relationships": relationship_results,
        "relevant_tables": sorted(relevant_tables)
    }