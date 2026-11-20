
from backend.ai_planner import plan_question
from backend.schema_retriever import retrieve_schema
from backend.dax_generator import generate_dax
from backend.dax_validator import validate_dax
from backend.dax_executor import execute_dax


def ask_powerbi(question):

    try:
        # 1. Generate AI plan
        plan = plan_question(question)

        if plan.get("needs_clarification") or not plan.get("metric"):
            return {
                "status": "clarification_required",
                "explanation": "Could not identify the requested metric or intent.",
                "dax": None,
                "data": None
            }

        # 2. Retrieve relevant live metadata
        schema = retrieve_schema(question)

        # 3. Generate DAX
        generated = generate_dax(
            question=question,
            plan=plan,
            schema=schema
        )

        if generated.get("status") != "success":
            return {
                "status": "generation_failed",
                "explanation": generated.get(
                    "explanation",
                    "Unable to generate a valid DAX query."
                ),
                "dax": None,
                "data": None
            }

        dax = generated["dax"]

        # 4. Validate DAX
        validation = validate_dax(dax, schema)

        if not validation.get("valid"):
            return {
                "status": "validation_failed",
                "explanation": "; ".join(validation.get("errors", [])),
                "dax": dax,
                "data": None
            }

        # 5. Execute against Power BI
        data = execute_dax(dax)

        return {
            "status": "success",
            "metric": plan.get("metric"),
            "intent": plan,
            "filters": plan.get("filters", []),
            "ranking": plan.get("ranking"),
            "explanation": "Query executed successfully",
            "dax": dax,
            "data": data
        }

    except Exception as e:

        return {
            "status": "error",
            "metric": None,
            "intent": None,
            "filters": [],
            "ranking": None,
            "explanation": str(e),
            "dax": None,
            "data": None
        }
