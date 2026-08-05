import json

from backend.ai.groq_client import generate_response


def generate_prescription(disease):

    prompt = f"""
You are a medical AI assistant.

The predicted disease is:

{disease}

Provide ONLY valid JSON.

Do NOT wrap the JSON in Markdown.
Do NOT use ```json.
Do NOT include any explanation.

Format:

{{
    "disease": "",
    "medicines": [
        {{
            "name": "",
            "dosage": "",
            "purpose": ""
        }}
    ],
    "precautions": [
        ""
    ],
    "lifestyle": [
        ""
    ],
    "disclaimer": "This is informational and must be reviewed by a licensed healthcare professional."
}}

Do not invent unsupported treatments.
If there are multiple common first-line options, mention them.
"""

    response = generate_response(prompt)

    response = response.strip()

    # Remove markdown code fences if present
    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

    if response.endswith("```"):
        response = response[:-3]

    response = response.strip()

    try:
        return json.loads(response)

    except json.JSONDecodeError:

        return {
            "disease": disease,
            "medicines": [],
            "precautions": [],
            "lifestyle": [],
            "disclaimer": "Unable to generate a structured prescription. Please consult a licensed healthcare professional."
        }