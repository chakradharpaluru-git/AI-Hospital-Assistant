import json

from insurance_rag.retriever import get_retriever
from backend.ai.groq_client import generate_response


def insurance_chat(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an AI Health Insurance Assistant.

Answer ONLY using the provided insurance documents.

If the answer is not available, reply:

"Information not available in the provided insurance documents."

Return ONLY valid JSON.

Do NOT wrap the JSON in Markdown.

Format:

{{
    "summary": "",
    "coverage": [],
    "required_documents": [],
    "claim_process": [],
    "notes": ""
}}

Insurance Context:

{context}

Question:

{question}
"""

    response = generate_response(prompt)

    response = response.strip()

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
            "coverage": [],
            "required_documents": [],
            "claim_process": [],
            "notes": ""
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