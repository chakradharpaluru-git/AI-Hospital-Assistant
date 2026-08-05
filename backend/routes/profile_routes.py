from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session


from backend.database.database import get_db


from backend.database.models import (
    User,
    Appointment,
    MedicalReport,
    Prescription,
    Insurance
)


from backend.schemas.profile_schema import (
    ProfileUpdate,
    ProfileResponse
)


from backend.services.profile_service import (
    get_profile,
    update_profile
)



router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)



# =====================================================
# GET PROFILE
# =====================================================

@router.get(
    "/{user_id}",
    response_model=ProfileResponse
)
def read_profile(

    user_id: int,

    db: Session = Depends(get_db)

):

    user = get_profile(
        db,
        user_id
    )


    if not user:

        raise HTTPException(

            status_code=404,

            detail="User not found"

        )


    return user





# =====================================================
# UPDATE PROFILE
# =====================================================

@router.put(
    "/{user_id}",
    response_model=ProfileResponse
)
def edit_profile(

    user_id: int,

    profile: ProfileUpdate,

    db: Session = Depends(get_db)

):

    user = update_profile(

        db,

        user_id,

        profile

    )


    if not user:

        raise HTTPException(

            status_code=404,

            detail="User not found"

        )


    return user





# =====================================================
# APPOINTMENT HISTORY
# =====================================================

@router.get(
    "/{user_id}/appointments"
)
def get_appointment_history(

    user_id:int,

    db:Session = Depends(get_db)

):


    appointments = (

        db.query(Appointment)

        .filter(

            Appointment.user_id == user_id

        )

        .all()

    )


    return appointments





# =====================================================
# MEDICAL REPORTS
# =====================================================

@router.get(
    "/{user_id}/reports"
)
def get_medical_reports(

    user_id:int,

    db:Session = Depends(get_db)

):


    reports = (

        db.query(MedicalReport)

        .filter(

            MedicalReport.user_id == user_id

        )

        .all()

    )


    return reports





# =====================================================
# PRESCRIPTIONS
# =====================================================

@router.get(
    "/{user_id}/prescriptions"
)
def get_prescription_history(

    user_id:int,

    db:Session = Depends(get_db)

):


    prescriptions = (

        db.query(Prescription)

        .filter(

            Prescription.user_id == user_id

        )

        .all()

    )


    return prescriptions





# =====================================================
# INSURANCE
# =====================================================

@router.get(
    "/{user_id}/insurance"
)
def get_insurance_details(

    user_id:int,

    db:Session = Depends(get_db)

):


    insurance = (

        db.query(Insurance)

        .filter(

            Insurance.user_id == user_id

        )

        .first()

    )


    if not insurance:

        return {

            "message":
            "No insurance details found"

        }


    return insurance