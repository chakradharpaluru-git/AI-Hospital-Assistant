from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.database import get_db

from backend.schemas.auth_schema import Register
from backend.schemas.auth_schema import Login

from backend.services.auth_service import register_user
from backend.services.auth_service import login_user

from backend.utils.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(

        user: Register,

        db: Session = Depends(get_db)

):

    new_user = register_user(db, user)

    if new_user is None:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )

    return {

        "message": "User Registered Successfully"

    }


@router.post("/login")
def login(

        user: Login,

        db: Session = Depends(get_db)

):

    db_user = login_user(

        db,

        user.email,

        user.password

    )

    if db_user is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid Credentials"

        )

    token = create_access_token(

        {

            "sub": db_user.email

        }

    )

    return {

        "access_token": token,

        "token_type": "Bearer"

    }