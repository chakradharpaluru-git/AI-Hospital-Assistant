from datetime import datetime

from pydantic import BaseModel



# =====================================================
# CREATE APPOINTMENT
# =====================================================

class AppointmentCreate(BaseModel):

    user_id: int

    patient_name: str

    doctor_name: str

    appointment_date: datetime



# =====================================================
# UPDATE APPOINTMENT
# =====================================================

class AppointmentUpdate(BaseModel):

    appointment_date: datetime