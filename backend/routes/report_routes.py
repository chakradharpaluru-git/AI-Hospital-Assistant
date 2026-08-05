from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from backend.services.report_service import save_report

router = APIRouter(

    prefix="/reports",

    tags=["Medical Reports"]

)


@router.post("/upload")
async def upload_report(

        file: UploadFile = File(...)

):

    result = save_report(file)

    if result is None:

        raise HTTPException(

            status_code=400,

            detail="Only PDF, DOCX and TXT files are allowed."

        )

    return result