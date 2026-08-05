from fastapi import APIRouter
from fastapi import HTTPException

from backend.schemas.disease_schema import (
    DiseaseInput,
    DiseaseResponse
)

from ml.predict_disease import predict

router = APIRouter(
    prefix="/disease",
    tags=["Disease Prediction"]
)


@router.post(
    "/predict",
    response_model=DiseaseResponse
)
def disease_prediction(data: DiseaseInput):

    try:

        result = predict(data.symptoms)

        return DiseaseResponse(
            disease=result["disease"],
            confidence=result["confidence"]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )