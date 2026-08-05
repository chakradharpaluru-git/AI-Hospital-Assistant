from sqlalchemy.orm import Session

from backend.database.models import User


def get_profile(db: Session, user_id: int):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def update_profile(
    db: Session,
    user_id: int,
    profile
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return None


    user.full_name = profile.full_name

    user.email = profile.email


    db.commit()

    db.refresh(user)


    return user