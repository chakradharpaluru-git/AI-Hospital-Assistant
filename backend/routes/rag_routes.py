from fastapi import APIRouter

from backend.schemas.rag_schema import QuestionRequest

from backend.ai.medical_rag import ask_medical_question


router = APIRouter(
    prefix="/rag",
    tags=["Medical RAG"]
)


@router.post("/ask")
def ask_question(
        data: QuestionRequest
):

    result = ask_medical_question(
        data.question
    )

    return {

        "question": data.question,

        "answer": result["answer"],

        "sources": result["sources"]

    }