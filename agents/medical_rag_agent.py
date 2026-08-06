from backend.ai.medical_rag import ask_medical_question


def medical_rag_agent(state):

    question = state["user_question"]


    result = ask_medical_question(
        question
    )


    return {

        "answer": result

    }