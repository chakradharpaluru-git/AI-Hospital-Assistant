from typing import List
from pydantic import BaseModel


class DiseaseInput(BaseModel):
    symptoms: List[str]


class DiseaseResponse(BaseModel):
    disease: str
    confidence: float