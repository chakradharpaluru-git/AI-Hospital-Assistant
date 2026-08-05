from pydantic import BaseModel


class EmergencyRequest(BaseModel):
    symptoms: str