from agents.state import AgentState


def supervisor_agent(state: AgentState):

    question = state["user_question"].lower()


    if "appointment" in question or "doctor" in question:

        agent = "appointment"


    elif "symptom" in question or "disease" in question:

        agent = "diagnosis"


    elif "medicine" in question or "drug" in question:

        agent = "prescription"


    elif "insurance" in question or "claim" in question:

        agent = "insurance"


    elif "emergency" in question or "urgent" in question:

        agent = "emergency"


    else:

        agent = "medical_rag"


    return {

        "next_agent": agent,

        "user_question": state["user_question"]

    }