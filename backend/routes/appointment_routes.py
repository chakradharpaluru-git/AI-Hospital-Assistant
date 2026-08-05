from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session


from backend.database.database import get_db


from backend.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate
)


from backend.services.appointment_service import (
    book_appointment,
    view_appointments,
    view_user_appointments,
    cancel_appointment,
    reschedule_appointment
)



router = APIRouter(

    prefix="/appointments",

    tags=["Appointments"]

)




# =====================================================
# BOOK
# =====================================================

@router.post("/book")
def book(

    data: AppointmentCreate,

    db: Session = Depends(get_db)

):

    return book_appointment(
        db,
        data
    )





# =====================================================
# VIEW ALL
# =====================================================

@router.get("/view")
def view(

    db: Session = Depends(get_db)

):

    return view_appointments(db)





# =====================================================
# VIEW USER APPOINTMENTS
# =====================================================

@router.get("/user/{user_id}")
def user_appointments(

    user_id: int,

    db: Session = Depends(get_db)

):

    return view_user_appointments(

        db,

        user_id

    )





# =====================================================
# RESCHEDULE
# =====================================================

@router.put("/reschedule/{appointment_id}")
def reschedule(

    appointment_id: int,

    data: AppointmentUpdate,

    db: Session = Depends(get_db)

):

    appointment = reschedule_appointment(

        db,

        appointment_id,

        data.appointment_date

    )


    if appointment is None:

        raise HTTPException(

            status_code=404,

            detail="Appointment not found"

        )


    return appointment





# =====================================================
# CANCEL
# =====================================================

@router.delete("/cancel/{appointment_id}")
def cancel(

    appointment_id: int,

    db: Session = Depends(get_db)

):

    appointment = cancel_appointment(

        db,

        appointment_id

    )


    if appointment is None:

        raise HTTPException(

            status_code=404,

            detail="Appointment not found"

        )


    return {

        "message":
        "Appointment cancelled successfully"

    }