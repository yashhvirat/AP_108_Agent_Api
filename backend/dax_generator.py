
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

    0. EXACT LIVE METADATA REFERENCES — HIGHEST PRIORITY

    The retrieved live semantic model metadata is the sole authority
    for physical table and column names.

    - Treat each column's "table" and "name" values as exact identifiers.
    - Copy table and column names character-for-character from metadata.
    - Preserve every space, slash, bracket, parenthesis and special character.
    - Never shorten, normalize, correct, paraphrase or reconstruct a name.
    - Do not infer a column name from the user's wording.
    - Do not replace a column with a similarly named column.
    - Do not use a column unless its exact table/name combination exists
      in the supplied metadata.
    - Use exact existing measure names from the measures metadata.
    - If a required column or measure is not present, return
      needs_clarification and identify the missing metadata.

    Examples:
    - If metadata contains "Locality (BL)", use [Locality (BL)].
      Never use [Locality].
    - If metadata contains "Ambulance Base Location", use that exact name.
      Never use [AmbulanceBase Location].
    - If metadata contains "Hospital Reached Time", never use
      [Hospital Reached].

    1. EXISTING MEASURES

    - Always prefer an existing measure when it correctly represents
    the requested metric.
    - Read the measure expression to understand its calculation.
    - Reference an existing measure using [Measure Name].
    - Never recreate an existing measure unnecessarily.
    - Verify that the selected measure is available in the metadata.
    - Consider whether the measure's internal filter logic could
    conflict with the mandatory global base filters.

    2. INLINE CALCULATIONS

    - If no suitable existing measure exists, generate an inline
    DAX calculation.
    - Use only verified table and column names from the metadata.
    - Never invent measure names, tables, columns or relationships.
    - If required metadata is missing, return needs_clarification.
    - Use CALCULATE when necessary to apply filter context.
    - Ensure every inline calculation respects both mandatory
    global base filters.

    
    3. AP108 BUSINESS DEFINITIONS

    Use the following AP108 business definitions when generating inline
    calculations.

    A. CASES AND DISPATCH OPERATIONS

    1. Cases
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - Represents unique ambulance events.

    2. Dispatches
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - Include only records where 'ERR'[Assign Time] is not blank.

    3. Abandoned
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - Assign Time is present AND At Scene Time is blank.

    4. ART Eligible
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - At Scene Time is present.

    5. At Scene Closures
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - Assign Time and At Scene Time are present.
    - Enroute Time, Hospital Reached Time and Hospital Handover Time
        are all blank.

    6. Completed Cases
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - 'ERR'[Hospital Reached Time] is not blank.
    - IMPORTANT: Use the exact column name Hospital Reached Time.
    - Never use 'ERR'[Hospital Reached].

    B. GOLDEN HOUR AND HOSPITAL TRANSFERS

    7. Golden Hour Eligible
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - Hospital Reached Time is present.
    - Hospital To Hospital Transfer is TRUE.

    8. Golden Hour Achieved
    - Use the existing Golden Hour achievement measure if available.
    - Otherwise, calculate only when all required timestamps and
        business rules are available in retrieved metadata.
    - Golden Hour target = 60 minutes.
    - Golden Hour duration is based on Assign Time to Hospital
        Reached Time.
    - Exclude Hospital-to-Hospital Transfer cases from standard
        Golden Hour performance calculations.

    9. IFT (Inter-Facility Transfer)
    - DISTINCTCOUNT of 'ERR'[Event Id].
    - Hospital To Hospital Transfer is TRUE.

    C. MDT MACHINE USAGE

    10. MDT Used
        - DISTINCTCOUNT of 'ERR'[Event Id].
        - Accepted Time is present AND at least one of:
        On Action Time or MDT Abandoned Time is present.

    11. MDT Not Used
        - Use the complement of MDT Used only when the relevant event
        population and business definition are clear.
        - Do not assume missing timestamps automatically mean an MDT
        failure.

    D. RESPONSE TIME AND SLA

    12. Average Response Time (ART)
        - Calculate using Assign Time to At Scene Time.
        - Use the existing ART measure if available.
        - Exclude records with missing required timestamps.

    13. ART SLA Target
        - Urban: 18 minutes.
        - Rural: 23 minutes.
        - Tribal: 33 minutes.
        - Determine locality using the appropriate model dimension
        and actual metadata.
        - Do not assume a locality when it is missing.

    14. ART SLA Achieved
        - Compare actual response time against the applicable locality
        target.
        - Use existing achievement measures when available.

    15. Golden Hour SLA
        - Target: 60 minutes.
        - Use Assign Time to Hospital Reached Time.
        - Exclude Hospital-to-Hospital Transfer cases.

    E. KILOMETRES AND ODOMETER

    16. KMS
        - Prefer the existing KMS measure.
        - If calculating inline, use verified odometer columns and the
        established business calculation.
        - Do not assume which odometer readings to subtract without
        checking the model metadata and existing measure expression.

    17. ODO Completeness
        - Prefer the existing ODO completeness measure.
        - Use verified On Action, At Scene and Hospital Reached
        odometer columns.
        - Do not invent missing odometer values.

    F. VEHICLE AND BASE LOCATION RULES

    18. Ambulance Filtering
        - All AP108 calculations must include:
        'ERR'[Ambulance/Feeder vehicle] = "Ambulance"

    19. Backup Base Exclusion
        - All AP108 calculations must exclude:
        'ERR'[Ambulance Base Location] = "Backup"
        - Apply:
        'ERR'[Ambulance Base Location] <> "Backup"

    20. Vehicle ID Exclusion
        - Exclude Vehicle Id values containing "FB" or "FE".
        - Handle blank Vehicle Id values safely.
        - Apply this rule when Vehicle Id is available in metadata.

    21. Neonatal
        - Neonatal vehicles/cases are identified using
        Ambulance Base Location containing "neonatal".
        - Apply only when the question requests neonatal analysis.

    G. IMPORTANT CALCULATION RULES

    - Use DISTINCTCOUNT of Event Id for event/case counts.
    - Never use COUNTROWS as a substitute for distinct event counts
    unless the requested metric explicitly requires row counts.
    - Apply the mandatory Ambulance and Backup filters to every query.
    - Preserve report-level and user-requested filters without
    overriding mandatory AP108 filters.
    - Use existing measures whenever their expressions correctly
    implement the requested definition.
    - Inspect existing measure expressions before selecting them.
    - Before using an existing measure, inspect its complete expression.
    - Confirm that it does not remove, override or bypass either mandatory
    global base filter through ALL, REMOVEFILTERS, ALLEXCEPT or other
    filter-modifying logic.
    - If the measure removes either mandatory filter, do not use it as-is.
    - Use a valid inline calculation that preserves the mandatory filters,
    or return needs_clarification if the calculation cannot be safely
    reconstructed.
    - Do not create duplicate inline calculations when a suitable
    existing measure is available.
    - Use exact table and column names from retrieved live metadata.
    - Do not invent or shorten column names.
    - For missing required metadata, return needs_clarification.
    - Do not silently substitute a different timestamp or column.
    - Ensure all date filters use the actual calendar relationship
    and the 'Calender'[Date] column when appropriate.


    4. MANDATORY GLOBAL BASE FILTERS

    The following two filters are compulsory for EVERY DAX query.

    They must NEVER be omitted, overridden or removed by the
    user's question.

    Rules:

    - Apply both filters to every metric and inline calculation.
    - Apply them to grouped and ungrouped queries.
    - Apply them to TOPN and BOTTOMN rankings.
    - Apply them alongside all date and user-requested filters.
    - User-requested filters must never remove or override these
    mandatory conditions.
    - Both filters must affect every returned calculation.
    - Never generate a query that bypasses these filters.
    - If either required column is missing from metadata, return
    needs_clarification instead of generating DAX without it.
    - Do not treat these filters as optional defaults.

    ADDITIONAL VEHICLE EXCLUSION:

    - Exclude Vehicle Id values containing "FB" or "FE"
    when the Vehicle Id column is available.
    - Handle blank Vehicle Id values safely.
    - Keep this additional exclusion separate from the two
    mandatory global base filters.

    5. DATE FILTERS

    - Use 'Calender'[Date] for date filtering when available.
    - Respect the exact date range from the planner.
    - Use inclusive start and end dates.
    - Do not invent date values.
    - Apply date filters alongside both mandatory global filters.
    - Do not allow date filters to remove mandatory base filters.

    6. GROUPING AND RANKING

    - Use the exact dimension specified by the planner.
    - Use SUMMARIZECOLUMNS for grouped results where appropriate.
    - Use TOPN for top ranking.
    - For bottom ranking, use TOPN with ascending sort order (ASC).
    - Do not use a BOTTOMN function.
    - Use the requested ranking count.
    - Sort results in the correct direction.
    - Apply mandatory filters before ranking.
    - Never rank results calculated without mandatory filters.

    
    CRITICAL: SUMMARIZECOLUMNS ARGUMENT ORDER

    SUMMARIZECOLUMNS arguments MUST appear in this order:

    1. Grouping columns.
    2. All filter-table expressions required by the user's question,
    such as date filters and additional user-requested filters.
    3. All output name/expression pairs.

    Never place a FILTER expression after an output
    name/expression pair.

    The mandatory AP108 base filters are applied separately
    by the DAX enforcement layer. Do not generate these two
    filters yourself:

    - 'ERR'[Ambulance/Feeder vehicle] = "Ambulance"
    - 'ERR'[Ambulance Base Location] <> "Backup"

    CORRECT EXAMPLE:

    EVALUATE
    SUMMARIZECOLUMNS(
        'Districts & Regions'[District],

        FILTER(
            'Calender',
            'Calender'[Date] >= DATE(2026, 10, 1) &&
            'Calender'[Date] <= DATE(2026, 10, 31)
        ),

        "Dispatches", [Dispatches]
    )

    INCORRECT EXAMPLE:

    SUMMARIZECOLUMNS(
        'Districts & Regions'[District],
        "Dispatches", [Dispatches],
        FILTER('Calender', ...)
    )


    7. UNGROUPED METRIC QUERIES

    If the user asks for a single metric without requesting
    a grouping, breakdown, ranking or trend:

    - Use CALCULATETABLE with ROW.
    - Do not use SUMMARIZECOLUMNS without grouping columns.
    - Reference an existing measure whenever suitable.
    - Apply applicable date filters and additional user-requested filters.
    - Do not generate the two mandatory AP108 base filters.
    The DAX enforcement layer adds them automatically.

    CORRECT EXAMPLE:

    EVALUATE
    CALCULATETABLE(
        ROW(
            "Dispatches", [Dispatches]
        )
    )


    8. FILTER IMPLEMENTATION BY QUERY TYPE

    A. UNGROUPED METRICS

    - Use CALCULATETABLE with ROW.
    - Apply both mandatory filters as filter arguments.
    - Include applicable date and user-requested filters.

    B. GROUPED METRICS

    - Use SUMMARIZECOLUMNS.
    - Include grouping columns first.
    - Include mandatory filters before output expressions.
    - Include applicable date and additional filters.
    - Ensure all returned calculations respect both filters.

    C. RANKING QUERIES

    - Use TOPN or appropriate bottom-ranking logic.
    - Generate the grouped result with mandatory filters.
    - Apply ranking to the already-filtered grouped result.
    - Do not rank unfiltered results.

    D. INLINE CALCULATIONS

    - Use CALCULATE where necessary.
    - Ensure both mandatory filters affect the calculation.
    - Do not calculate a metric outside the mandatory filter context.

    E. FILTER CONSISTENCY

    - Both mandatory filters must affect every returned metric.
    - Do not merely include the filter expressions in an
    unrelated part of the DAX query.
    - Never bypass mandatory filters through an alternative
    calculation or intermediate table.

    9. DAX QUERY FORMAT

    - Return a complete DAX query beginning with EVALUATE.
    - Use valid Power BI DAX syntax.
    - Use actual semantic model table and column names.
    - Do not return SQL.
    - Do not return calculated-column or calculated-table definitions.
    - Do not execute the query.
    - Generate read-only DAX queries only.

    10. SAFETY

    - Never generate DAX that attempts to modify model data,
    metadata, permissions or security settings.
    - Never invent metadata.
    - If the request cannot be answered with the supplied metadata,
    explain which metadata is missing.
    - Do not generate a successful query if mandatory filter
    columns are unavailable.

    11. FINAL SELF-CHECK

    Before returning the DAX:

    - Check every table and column against supplied metadata.
    - Check every measure against supplied metadata.
    - Check SUMMARIZECOLUMNS argument ordering.
    - Check that all filters appear before output name/expression pairs.
    - Check TOPN ranking direction and count.
    - Check that the query begins with EVALUATE.
    - Verify both mandatory global base filters are applied.
    - Verify no user-requested filter overrides either condition.
    - Verify every returned metric respects both mandatory filters.
    - For ungrouped metrics, verify CALCULATETABLE and ROW usage.
    - For grouped metrics, verify mandatory filters are applied
    within the grouped calculation.
    - For rankings, verify mandatory filters are applied before TOPN.
    - If either mandatory filter is missing, do not return success.
    - If the query structure is invalid, return needs_clarification.

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
