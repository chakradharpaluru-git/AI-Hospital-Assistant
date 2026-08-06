from fastapi import APIRouter

from backend.ai.medical_rag import ask_medical_question


router = APIRouter(
    prefix="/medical",
    tags=["Medical RAG"]
)



@router.post("/ask")
def medical_question(data:dict):

    question = data.get(
        "question"
    )


    result = ask_medical_question(
        question
    )


    return result
