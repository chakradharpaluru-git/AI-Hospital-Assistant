from backend.ai.insurance_rag import insurance_chat


def insurance_agent(state):

    response = insurance_chat(
        state["user_question"]
    )

    return {
        "answer": response["answer"],
        "sources": response["sources"]
    }