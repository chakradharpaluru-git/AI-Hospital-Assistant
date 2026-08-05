import os

from pypdf import PdfReader

from docx import Document


def extract_text(filepath):

    extension = os.path.splitext(filepath)[1].lower()

    if extension == ".pdf":

        reader = PdfReader(filepath)

        text = ""

        for page in reader.pages:

            text += page.extract_text()

        return text

    elif extension == ".docx":

        doc = Document(filepath)

        return "\n".join(
            p.text for p in doc.paragraphs
        )

    elif extension == ".txt":

        with open(
            filepath,
            encoding="utf-8"
        ) as file:

            return file.read()

    return ""