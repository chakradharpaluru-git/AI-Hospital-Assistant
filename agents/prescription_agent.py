from backend.ai.prescription_generator import generate_prescription


def prescription_agent(state):

    disease = state.get("disease")

    result = generate_prescription(disease)

    return {

        "answer": result

    }