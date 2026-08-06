from fastapi import APIRouter

from agents.graph import agent_graph


router = APIRouter(
    prefix="/agents",
    tags=["Multi Agents"]
)



@router.post("/query")
def agent_query(data: dict):


    question = data.get(
        "question"
    )


    if not question:

        return {
            "error":
            "question field required"
        }



    result = agent_graph.invoke(

        {
            "user_question": question,

            "next_agent": "",

            "answer": None

        }

    )


    return {

        "question": question,

        "answer": result["answer"]

    }