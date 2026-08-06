import json

from rag.retriever import get_retriever
from backend.ai.groq_client import generate_response


def ask_medical_question(question: str):

    retriever = get_retriever()

    docs = retriever.invoke(question)


    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )


    prompt = f"""
You are a medical AI assistant.

Answer only using the provided medical documents.

If the information is not directly available, do not invent facts.
Use only medically safe general guidance from the provided context.

Return ONLY valid JSON.

Format:

{{
    "summary": "",
    "key_guidelines": [],
    "medications": [],
    "precautions": [],
    "when_to_consult_doctor": ""
}}


Medical Context:

{context}


Question:

{question}

"""


    response = generate_response(prompt)


    response = response.strip()


    # Remove markdown formatting
    if response.startswith("```json"):
        response = response.replace(
            "```json",
            "",
            1
        )

    if response.startswith("```"):
        response = response.replace(
            "```",
            "",
            1
        )

    if response.endswith("```"):
        response = response[:-3]


    response = response.strip()


    try:

        result = json.loads(response)


    except json.JSONDecodeError:

        result = {

            "summary": response,

            "key_guidelines": [],

            "medications": [],

            "precautions": [],

            "when_to_consult_doctor": "Mention situations where medical evaluation is recommended based on the document."

        }


    sources = list(
        {
            doc.metadata.get(
                "source",
                "Unknown"
            )
            for doc in docs
        }
    )


    return {

        "answer": result,

        "sources": sources

    }