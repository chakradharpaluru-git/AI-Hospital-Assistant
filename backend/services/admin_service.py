from sqlalchemy.orm import Session

from backend.database.models import (
    User,
    Appointment,
    MedicalReport
)


def get_all_users(db: Session):

    return db.query(User).all()



def get_all_appointments(db: Session):

    return db.query(Appointment).all()



def get_all_reports(db: Session):

    return db.query(MedicalReport).all()



def get_analytics(db: Session):

    return {

        "total_users":
            db.query(User).count(),

        "total_appointments":
            db.query(Appointment).count(),

        "total_reports":
            db.query(MedicalReport).count()

    }