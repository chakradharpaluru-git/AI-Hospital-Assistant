from fastapi import FastAPI

from backend.database.database import Base, engine


# =====================================================
# IMPORT MODELS FIRST
# =====================================================
# This registers tables with SQLAlchemy

from backend.database import models


# =====================================================
# IMPORT ROUTERS
# =====================================================

from backend.routes.auth_routes import router as auth_router
from backend.routes.disease_routes import router as disease_router
from backend.routes.report_routes import router as report_router
from backend.routes.report_summary_routes import router as report_summary_router
from backend.routes.rag_routes import router as rag_router
from backend.routes.agent_routes import router as agent_router
from backend.routes.appointment_routes import router as appointment_router
from backend.routes.prescription_routes import router as prescription_router
from backend.routes.insurance_routes import router as insurance_router
from backend.routes.emergency_routes import router as emergency_router
from backend.routes.profile_routes import router as profile_router
from backend.routes.admin_routes import router as admin_router

# =====================================================
# CREATE DATABASE TABLES
# =====================================================

Base.metadata.create_all(
    bind=engine
)



# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(

    title="AI Hospital Assistant",

    version="1.0"

)



# =====================================================
# REGISTER ROUTERS
# =====================================================

app.include_router(
    auth_router
)


app.include_router(
    disease_router
)


app.include_router(
    report_router
)


app.include_router(
    report_summary_router
)


app.include_router(
    rag_router
)


app.include_router(
    agent_router
)


app.include_router(
    appointment_router
)


app.include_router(
    prescription_router
)


app.include_router(
    insurance_router
)


app.include_router(
    emergency_router
)

app.include_router(profile_router)
app.include_router(
    admin_router
)

# =====================================================
# BASIC ROUTES
# =====================================================


@app.get("/")
def home():

    return {

        "message":
        "AI Hospital Assistant Running"

    }



@app.get("/health")
def health():

    return {

        "status":
        "Healthy"

    }