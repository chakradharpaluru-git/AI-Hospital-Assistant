from pydantic import BaseModel


class InsuranceQuestion(BaseModel):

    question: str