import os

from fastapi import APIRouter, UploadFile, File

from backend.services.file_reader import extract_text
from backend.ai.report_summarizer import summarize_report


router = APIRouter(
    prefix="/medical-report",
    tags=["Medical Report AI"]
)


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/summarize")
async def summarize(file: UploadFile = File(...)):

    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    # Save uploaded file
    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())


    # Extract text
    text = extract_text(filepath)


    # Gemini summary
    result = summarize_report(text)


    return {

        "filename": file.filename,

        "analysis": result

    }