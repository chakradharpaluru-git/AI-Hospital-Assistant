from fastapi import APIRouter

from agents.graph import agent_graph


router = APIRouter(
    prefix="/agents",
    tags=["Multi Agents"]
)


@router.post("/query")
def agent_query(data:dict):


    result = agent_graph.invoke(

        {

            "user_question":
            data["question"]

        }

    )


    return {

        "answer":
        result["answer"]

    }