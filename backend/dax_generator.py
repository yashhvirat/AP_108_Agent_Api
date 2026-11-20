
import json
import re

from backend.llm_engine import generate_response


def build_dax_prompt(question, plan, schema):

    metadata = {
        "measures": schema.get("measures", []),
        "columns": schema.get("columns", []),
        "relationships": schema.get("relationships", []),
        "relevant_tables": schema.get("relevant_tables", [])
    }

    metadata_json = json.dumps(
        metadata,
        ensure_ascii=False,
        indent=2,
        default=str
    )

    plan_json = json.dumps(
        plan,
        ensure_ascii=False,
        indent=2,
        default=str
    )

    prompt = f"""
You are an expert Power BI DAX developer.

Your task is to generate a valid DAX query for the AP108 Ambulance
Analytics Power BI semantic model.

USER QUESTION:
{question}

AI PLANNER OUTPUT:
{plan_json}

RETRIEVED LIVE SEMANTIC MODEL METADATA:
{metadata_json}


IMPORTANT RULES:

1. EXISTING MEASURES

- Always prefer an existing measure when it correctly represents
  the requested metric.
- Read the measure expression to understand its calculation.
- Reference an existing measure using [Measure Name].
- Never recreate an existing measure unnecessarily.

2. INLINE CALCULATIONS

- If no suitable existing measure exists, generate an inline
  DAX calculation.
- Use only verified table and column names from the metadata.
- Never invent measure names, tables, columns or relationships.
- If required metadata is missing, return needs_clarification.

3. AP108 BUSINESS DEFINITIONS

- Cases = DISTINCTCOUNT of Event Id.
- Dispatches = distinct Event Id where Assign Time is not blank.
- Abandoned = Assign Time is present and At Scene is blank.
- ART Eligible = At Scene is present.
- At Scene Closures = Assign Time and At Scene are present,
  while Enroute, Hospital Reached and Hospital Handover are blank.
- Golden Hour Eligible = Hospital Reached is present and
  Hospital To Hospital Transfer is true.
- IFT = Hospital To Hospital Transfer is true.
- Completed = Hospital Reached is present.
- MDT Used = Accepted is present AND (On Action or Mdt Abandoned
  is present).

Only apply a definition if all required columns are available
in the retrieved metadata.

4. COMMON AP108 FILTERS

Apply these default filters when their columns are available,
unless the user explicitly requests otherwise:

- 'ERR'[Ambulance/Feeder vehicle] = "Ambulance"
- 'ERR'[Ambulance Base Location] <> "Backup"

Exclude vehicle IDs containing FB or FE when the Vehicle Id
column is available. Handle blank vehicle IDs safely.

5. DATE FILTERS

- Use 'Calender'[Date] for date filtering when available.
- Respect the exact date range from the planner.
- Use inclusive start and end dates.
- Do not invent date values.

6. GROUPING AND RANKING

- Use the exact dimension specified by the planner.
- Use SUMMARIZECOLUMNS for grouped results where appropriate.
- Use TOPN for top/bottom ranking.
- Use the requested ranking count.
- Sort results in the correct direction.

CRITICAL: SUMMARIZECOLUMNS ARGUMENT ORDER

SUMMARIZECOLUMNS arguments MUST appear in this order:

1. Grouping columns.
2. All filter-table expressions.
3. All output name/expression pairs.

Never place a FILTER expression after an output
name/expression pair.

CORRECT EXAMPLE:

SUMMARIZECOLUMNS(
    'Districts & Regions'[District],

    FILTER(
        'Calender',
        'Calender'[Date] >= DATE(2026, 10, 1) &&
        'Calender'[Date] <= DATE(2026, 10, 31)
    ),

    FILTER(
        'ERR',
        'ERR'[Ambulance/Feeder vehicle] = "Ambulance" &&
        'ERR'[Ambulance Base Location] <> "Backup"
    ),

    "Dispatches", [Dispatches]
)

INCORRECT EXAMPLE:

SUMMARIZECOLUMNS(
    'Districts & Regions'[District],
    "Dispatches", [Dispatches],
    FILTER('Calender', ...)
)

The incorrect example places a filter expression after
an output name/expression pair.

7. DAX QUERY FORMAT

- Return a complete DAX query beginning with EVALUATE.
- Use valid Power BI DAX syntax.
- Use actual semantic model table and column names.
- Do not return SQL.
- Do not return calculated-column or calculated-table definitions.
- Do not execute the query.

8. SAFETY

- Generate read-only DAX queries only.
- Never generate DAX that attempts to modify model data,
  metadata, permissions or security settings.
- If the request cannot be answered with the supplied metadata,
  explain which metadata is missing.

9. FINAL SELF-CHECK

Before returning the DAX:

- Check every table and column against supplied metadata.
- Check every measure against supplied metadata.
- Check SUMMARIZECOLUMNS argument ordering.
- Check that all filters appear before output name/expression pairs.
- Check TOPN ranking direction and count.
- Check that the query begins with EVALUATE.

RETURN ONLY VALID JSON.
Do not use Markdown code fences.

Required JSON structure:

{{
    "status": "success or needs_clarification",
    "dax": "complete DAX query or null",
    "selected_measure": "existing measure name or null",
    "calculation_type": "existing_measure or inline_calculation",
    "explanation": "brief explanation",
    "assumptions": [],
    "missing_metadata": []
}}
"""

    return prompt


def parse_json_response(response_text):

    text = response_text.strip()

    text = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        text,
        flags=re.IGNORECASE
    ).strip()

    return json.loads(text)


def generate_dax(question, plan, schema):

    prompt = build_dax_prompt(
        question=question,
        plan=plan,
        schema=schema
    )

    response = generate_response(prompt)

    try:
        result = parse_json_response(response)

    except json.JSONDecodeError as error:

        raise ValueError(
            f"Gemini returned invalid JSON: {error}\n"
            f"Response: {response[:1000]}"
        )

    required_fields = [
        "status",
        "dax",
        "selected_measure",
        "calculation_type",
        "explanation",
        "assumptions",
        "missing_metadata"
    ]

    for field in required_fields:

        if field not in result:
            raise ValueError(
                f"Missing field in Gemini response: {field}"
            )

    if result["status"] == "success":

        dax = result.get("dax")

        if not isinstance(dax, str) or not dax.strip():
            raise ValueError(
                "Gemini reported success but did not return DAX."
            )

        if not dax.strip().upper().startswith("EVALUATE"):
            raise ValueError(
                "Generated DAX must begin with EVALUATE."
            )

    elif result["status"] == "needs_clarification":

        if not result.get("explanation"):
            result["explanation"] = (
                "More information is required to generate the query."
            )

    else:

        raise ValueError(
            f"Unexpected DAX generation status: {result['status']}"
        )

    return result
