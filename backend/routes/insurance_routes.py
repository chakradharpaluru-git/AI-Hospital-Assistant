from fastapi import APIRouter

from backend.schemas.insurance_schema import InsuranceQuestion

from backend.ai.insurance_rag import insurance_chat


router = APIRouter(

    prefix="/insurance",

    tags=["Insurance"]

)


@router.post("/ask")
def ask(data: InsuranceQuestion):

    answer = insurance_chat(

        data.question

    )

    return {

        "question": data.question,

        "answer": answer

    }