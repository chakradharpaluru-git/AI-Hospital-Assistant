from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from backend.database.database import Base


# =====================================================
# USER
# =====================================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )



# =====================================================
# APPOINTMENT
# =====================================================

class Appointment(Base):

    __tablename__ = "appointments"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    patient_name = Column(
        String(100),
        nullable=False
    )


    doctor_name = Column(
        String(100),
        nullable=False
    )


    appointment_date = Column(
        DateTime,
        nullable=False
    )


    status = Column(
        String(20),
        nullable=False,
        default="Booked"
    )



# =====================================================
# MEDICAL REPORT
# =====================================================

class MedicalReport(Base):

    __tablename__ = "medical_reports"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    patient_name = Column(
        String(100),
        nullable=False
    )


    filename = Column(
        String(255),
        nullable=False
    )


    summary = Column(
        Text
    )


    uploaded_at = Column(
        DateTime
    )



# =====================================================
# PRESCRIPTION
# =====================================================

class Prescription(Base):

    __tablename__ = "prescriptions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    patient_name = Column(
        String(100),
        nullable=False
    )


    diagnosis = Column(
        Text
    )


    medicines = Column(
        Text
    )


    instructions = Column(
        Text
    )


    created_at = Column(
        DateTime
    )



# =====================================================
# INSURANCE
# =====================================================

class Insurance(Base):

    __tablename__ = "insurance"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    patient_name = Column(
        String(100),
        nullable=False
    )


    policy_number = Column(
        String(100)
    )


    company = Column(
        String(100)
    )


    policy_type = Column(
        String(100)
    )


    coverage = Column(
        String(200)
    )


    uploaded_at = Column(
        DateTime
    )



# =====================================================
# CHAT HISTORY
# =====================================================

class ChatHistory(Base):

    __tablename__ = "chat_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    question = Column(
        Text
    )


    answer = Column(
        Text
    )


    created_at = Column(
        DateTime
    )