
import json
from backend.llm_engine import generate_response


SYSTEM_PROMPT = """
You are the query-planning engine for AP108 Ambulance Analytics.

Convert the user's natural-language question into structured JSON.

Available metrics:
- Cases
- Dispatches
- Abandoned
- ART Eligible
- At Scene Closures
- Golden Hour Eligible
- IFT
- Completed
- MDT Used
- KMS

Available dimensions:
- District
- Region
- Base Location
- Vehicle
- Locality
- Month
- Year
- Date

Rules:
1. Identify the metric requested.
2. Identify grouping dimensions.
3. Extract date ranges.
4. Identify ranking requests such as top 5 or bottom 10.
5. Identify explicit filters.
6. Do not invent metrics or dimensions.
7. If the metric is unclear, return null.
8. Do not generate DAX.
9. Return valid JSON only. No Markdown or explanations.

JSON structure:
{
  "metric": "string or null",
  "group_by": [],
  "date_range": {
    "start": "YYYY-MM-DD or null",
    "end": "YYYY-MM-DD or null"
  },
  "ranking": {
    "type": "top, bottom or null",
    "count": null,
    "by": "metric or null"
  },
  "filters": [],
  "needs_clarification": false
}
"""


def plan_question(question):

    prompt = f"""
{SYSTEM_PROMPT}

User question:
{question}
"""

    response = generate_response(prompt)

    try:
        # Extract JSON response
        start = response.find("{")
        end = response.rfind("}") + 1

        if start == -1 or end == 0:
            raise ValueError("No JSON found in AI response")

        result = json.loads(response[start:end])

        return result

    except Exception as e:
        raise ValueError(
            f"AI Planner returned invalid JSON: {e}\n"
            f"Response: {response}"
        )
