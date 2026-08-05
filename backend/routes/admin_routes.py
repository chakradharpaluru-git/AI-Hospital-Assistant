from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session


from backend.database.database import get_db


from backend.services.admin_service import (
    get_all_users,
    get_all_appointments,
    get_all_reports,
    get_analytics
)


router = APIRouter(

    prefix="/admin",

    tags=["Admin"]

)



# ===============================
# USERS
# ===============================

@router.get("/users")
def users(

    db: Session = Depends(get_db)

):

    return get_all_users(db)



# ===============================
# APPOINTMENTS
# ===============================

@router.get("/appointments")
def appointments(

    db: Session = Depends(get_db)

):

    return get_all_appointments(db)



# ===============================
# REPORTS
# ===============================

@router.get("/reports")
def reports(

    db: Session = Depends(get_db)

):

    return get_all_reports(db)



# ===============================
# ANALYTICS
# ===============================

@router.get("/analytics")
def analytics(

    db: Session = Depends(get_db)

):

    return get_analytics(db)