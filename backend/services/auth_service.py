from sqlalchemy.orm import Session

from backend.database.models import User
from backend.utils.security import hash_password
from backend.utils.security import verify_password


def register_user(db: Session, user):

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:
        return None

    new_user = User(
    full_name=user.full_name,
    email=user.email,
    password=hash_password(user.password)
)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user