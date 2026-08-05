from pydantic import BaseModel


class UserResponse(BaseModel):

    id: int
    full_name: str
    email: str

    class Config:
        from_attributes = True


class AnalyticsResponse(BaseModel):

    total_users: int
    total_appointments: int
    total_reports: int