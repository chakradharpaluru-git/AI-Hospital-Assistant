def supervisor_agent(state):

    question = state["user_question"].lower()


    if any(
        word in question
        for word in [
            "symptom",
            "disease",
            "diabetes",
            "fever",
            "pain",
            "health"
        ]
    ):

        next_agent = "medical_rag"


    elif "appointment" in question:

        next_agent = "appointment"


    elif "prescription" in question:

        next_agent = "prescription"


    elif "insurance" in question:

        next_agent = "insurance"


    elif "emergency" in question:

        next_agent = "emergency"


    else:

        next_agent = "medical_rag"



    return {

        "next_agent": next_agent

    }