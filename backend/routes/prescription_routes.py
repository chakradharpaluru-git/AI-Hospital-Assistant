from fastapi import APIRouter

from backend.schemas.prescription_schema import PrescriptionRequest

from backend.ai.prescription_generator import generate_prescription


router = APIRouter(

    prefix="/prescription",

    tags=["Prescription"]

)


@router.post("/generate")
def prescription(data: PrescriptionRequest):

    result = generate_prescription(

        data.disease

    )

    return {

        "prescription": result

    }