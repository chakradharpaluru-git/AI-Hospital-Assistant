import json

from rag.retriever import get_retriever
from backend.ai.groq_client import generate_response


def ask_medical_question(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are a medical AI assistant.

Answer ONLY using the provided medical context.

If the answer is not present in the context, reply:
"Information not available in the provided medical documents."

Return ONLY valid JSON.

Rules:
- Do NOT wrap the JSON inside ```json or ``` fences.
- Do NOT include explanations before or after the JSON.
- Return exactly one JSON object.

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

    # Remove whitespace
    response = response.strip()

    # Remove markdown code blocks if Groq returns them
    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

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
            "when_to_consult_doctor": ""
        }

    sources = list(
        {
            doc.metadata.get("source", "Unknown")
            for doc in docs
        }
    )

    return {
        "answer": result,
        "sources": sources
    }