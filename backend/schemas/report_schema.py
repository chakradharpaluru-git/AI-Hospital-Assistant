from pydantic import BaseModel


class ReportResponse(BaseModel):

    filename: str

    file_type: str

    file_size: int

    message: str