from fastapi import APIRouter

from backend.schemas.emergency_schema import EmergencyRequest

from backend.ai.emergency_ai import emergency_assessment


router = APIRouter(
    prefix="/emergency",
    tags=["Emergency"]
)


@router.post("/assess")
def assess(data: EmergencyRequest):

    result = emergency_assessment(
        data.symptoms
    )

    return result