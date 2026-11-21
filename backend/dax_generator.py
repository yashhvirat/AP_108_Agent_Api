
import json
import re
from pathlib import Path
from functools import lru_cache

from backend.llm_engine import generate_response


@lru_cache(maxsize=1)
def load_dax_reference():

    project_root = Path(__file__).resolve().parent.parent

    reference_path = (
        project_root
        / "docs"
        / "ap108_dax_reference_revised.md"
    )

    if not reference_path.exists():
        raise FileNotFoundError(
            f"DAX reference not found: {reference_path}"
        )

    return reference_path.read_text(
        encoding="utf-8"
    )

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

    dax_reference = load_dax_reference()
    
    prompt = f"""
    You are an expert Power BI DAX developer.

    Your task is to generate a valid DAX query for the AP108 Ambulance
    Analytics Power BI semantic model.

    {dax_reference}

    USER QUESTION:
    {question}

    AI PLANNER OUTPUT:
    {plan_json}

    RETRIEVED LIVE SEMANTIC MODEL METADATA:
    {metadata_json}
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
