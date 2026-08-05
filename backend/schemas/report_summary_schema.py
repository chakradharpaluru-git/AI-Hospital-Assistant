from pydantic import BaseModel


class ReportRequest(BaseModel):

    filename: str