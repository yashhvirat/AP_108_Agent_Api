
from backend.ai_planner import plan_question
from backend.schema_retriever import retrieve_schema
from backend.dax_generator import generate_dax
from backend.dax_validator import validate_dax
from backend.dax_executor import execute_dax
from backend.dax_enforcer import enforce_dax



def ask_powerbi(question):

    dax = None
    plan = None

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
        schema = retrieve_schema(question, plan=plan)

        # 3. Generate DAX
        generated = generate_dax(
            question=question,
            plan=plan,
            schema=schema
        )

        print("\n========== DAX GENERATION RESULT ==========")
        print(generated)
        print("==========================================")

        if generated.get("status") != "success":
            return {
                "status": "generation_failed",
                "explanation": generated.get(
                    "explanation",
                    "Unable to generate a valid DAX query."
                ),
                "dax": generated.get("dax"),
                "data": None
            }

        dax = generated["dax"]

        # 4. Enforce mandatory AP108 filters
        enforcement = enforce_dax(dax, schema)

        print("\n========== DAX ENFORCEMENT ==========")
        print(enforcement)
        print("====================================")

        if not enforcement.get("valid"):
            return {
                "status": "enforcement_failed",
                "explanation": "; ".join(
                    enforcement.get("errors", [])
                ),
                "dax": dax,
                "data": None
            }

        dax = enforcement["dax"]

        # 5. Validate DAX
        validation = validate_dax(dax, schema)

        print("\n========== DAX VALIDATION ==========")
        print(validation)
        print("====================================")

        if not validation.get("valid"):
            return {
                "status": "validation_failed",
                "explanation": "; ".join(validation.get("errors", [])),
                "dax": dax,
                "data": None
            }

        # 5. Execute against Power BI
        print("\nExecuting DAX against Power BI...")

        data = execute_dax(dax)

        # print("\n========== POWER BI RESULT ==========")
        # print(data)
        # print("Result type:", type(data))
        # print("====================================")

        if data is None:
            return {
                "status": "execution_failed",
                "metric": plan.get("metric"),
                "intent": plan,
                "explanation": "Power BI returned no DataFrame.",
                "dax": dax,
                "data": None
            }

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

        print("\n========== AI ENGINE ERROR ==========")
        print(repr(e))
        print("=====================================")

        return {
            "status": "error",
            "metric": plan.get("metric") if plan else None,
            "intent": plan,
            "filters": plan.get("filters", []) if plan else [],
            "ranking": plan.get("ranking") if plan else None,
            "explanation": str(e),
            "dax": dax,
            "data": None
        }

