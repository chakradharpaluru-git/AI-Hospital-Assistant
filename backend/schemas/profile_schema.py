from pydantic import BaseModel, EmailStr


class ProfileUpdate(BaseModel):
    full_name: str
    email: EmailStr


class ProfileResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True