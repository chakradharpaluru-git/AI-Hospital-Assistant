from backend.ai.medical_rag import ask_medical_question


def diagnosis_agent(state):

    question = state["user_question"]


    response = ask_medical_question(
        question
    )


    return {

        "answer": response["answer"],

        "sources": response["sources"]

    }