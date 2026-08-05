from backend.ai.medical_rag import ask_medical_question


def medical_rag_agent(state):

    response = ask_medical_question(
        state["user_question"]
    )

    return {

        "answer": response["answer"],

        "sources": response["sources"]

    }