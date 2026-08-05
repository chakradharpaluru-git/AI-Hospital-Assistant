from sqlalchemy.orm import Session

from backend.database.models import Appointment



# =====================================================
# BOOK APPOINTMENT
# =====================================================

def book_appointment(
    db: Session,
    data
):

    appointment = Appointment(

        user_id=data.user_id,

        patient_name=data.patient_name,

        doctor_name=data.doctor_name,

        appointment_date=data.appointment_date,

        status="Booked"
    )


    db.add(appointment)

    db.commit()

    db.refresh(appointment)


    return appointment




# =====================================================
# VIEW ALL APPOINTMENTS
# =====================================================

def view_appointments(
    db: Session
):

    return (
        db.query(Appointment)
        .all()
    )




# =====================================================
# VIEW USER APPOINTMENTS
# =====================================================

def view_user_appointments(
    db: Session,
    user_id: int
):

    return (
        db.query(Appointment)
        .filter(
            Appointment.user_id == user_id
        )
        .all()
    )




# =====================================================
# CANCEL APPOINTMENT
# =====================================================

def cancel_appointment(
    db: Session,
    appointment_id: int
):

    appointment = (
        db.query(Appointment)
        .filter(
            Appointment.id == appointment_id
        )
        .first()
    )


    if not appointment:

        return None


    appointment.status = "Cancelled"


    db.commit()

    db.refresh(appointment)


    return appointment




# =====================================================
# RESCHEDULE APPOINTMENT
# =====================================================

def reschedule_appointment(
    db: Session,
    appointment_id: int,
    new_date
):

    appointment = (
        db.query(Appointment)
        .filter(
            Appointment.id == appointment_id
        )
        .first()
    )


    if not appointment:

        return None


    appointment.appointment_date = new_date

    appointment.status = "Rescheduled"


    db.commit()

    db.refresh(appointment)


    return appointment