import os

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".txt"
]


def save_report(file):

    filename = file.filename

    extension = os.path.splitext(filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        return None

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    with open(filepath, "wb") as buffer:

        buffer.write(file.file.read())

    return {

        "filename": filename,

        "file_type": extension,

        "file_size": os.path.getsize(filepath),

        "message": "Medical Report Uploaded Successfully"

    }