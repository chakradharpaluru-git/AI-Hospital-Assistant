
from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError
from jose import jwt

from backend.config import settings


# ==========================================================
# PASSWORD HASHER
# ==========================================================

pwd_hasher = PasswordHasher()


# ==========================================================
# PASSWORD FUNCTIONS
# ==========================================================

def hash_password(password: str) -> str:
    return pwd_hasher.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    try:
        return pwd_hasher.verify(
            hashed_password,
            plain_password
        )

    except (VerifyMismatchError, VerificationError):
        return False


# ==========================================================
# JWT
# ==========================================================

def create_access_token(
    data: dict,
    expires_delta=None
):

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=30
        )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt

