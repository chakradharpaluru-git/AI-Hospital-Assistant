from pydantic import BaseModel


class PrescriptionRequest(BaseModel):

    disease: str