from backend.ai.emergency_ai import emergency_assessment


def emergency_agent(state):

    result = emergency_assessment(
        state["user_question"]
    )

    return {

        "answer": result

    }