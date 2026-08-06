from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext


# ==============================
# JWT CONFIGURATION
# ==============================

SECRET_KEY = "hospital_secret"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60



# ==============================
# PASSWORD HASHING
# ==============================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



def hash_password(password: str) -> str:

    # bcrypt supports only 72 bytes
    password = password[:72]

    return pwd_context.hash(password)



def verify_password(
        plain_password: str,
        hashed_password: str
):

    plain_password = plain_password[:72]

    return pwd_context.verify(
        plain_password,
        hashed_password
    )



# ==============================
# CREATE JWT TOKEN
# ==============================

def create_access_token(data: dict):

    to_encode = data.copy()


    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )


    to_encode.update(
        {
            "exp": expire
        }
    )


    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )