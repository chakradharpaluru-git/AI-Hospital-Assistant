from langgraph.graph import StateGraph, END

from agents.state import AgentState

from agents.supervisor_agent import supervisor_agent

from agents.appointment_agent import appointment_agent
from agents.diagnosis_agent import diagnosis_agent
from agents.prescription_agent import prescription_agent
from agents.insurance_agent import insurance_agent
from agents.emergency_agent import emergency_agent
from agents.medical_rag_agent import medical_rag_agent



workflow = StateGraph(AgentState)



workflow.add_node(
    "supervisor",
    supervisor_agent
)


workflow.add_node(
    "appointment",
    appointment_agent
)


workflow.add_node(
    "diagnosis",
    diagnosis_agent
)


workflow.add_node(
    "prescription",
    prescription_agent
)


workflow.add_node(
    "insurance",
    insurance_agent
)


workflow.add_node(
    "emergency",
    emergency_agent
)


workflow.add_node(
    "medical_rag",
    medical_rag_agent
)



workflow.set_entry_point(
    "supervisor"
)



workflow.add_conditional_edges(

    "supervisor",

    lambda state: state["next_agent"],

    {

        "appointment":"appointment",

        "diagnosis":"diagnosis",

        "prescription":"prescription",

        "insurance":"insurance",

        "emergency":"emergency",

        "medical_rag":"medical_rag"

    }

)



workflow.add_edge("appointment", END)
workflow.add_edge("diagnosis", END)
workflow.add_edge("prescription", END)
workflow.add_edge("insurance", END)
workflow.add_edge("emergency", END)
workflow.add_edge("medical_rag", END)



agent_graph = workflow.compile()