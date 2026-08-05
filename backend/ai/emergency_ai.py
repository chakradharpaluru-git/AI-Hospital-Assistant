import json
import re

from backend.ai.groq_client import generate_response


def emergency_assessment(symptoms: str):
    prompt = f"""
You are an Emergency Medical AI Assistant.

Based ONLY on the symptoms below, provide a TRIAGE assessment.

Symptoms:
{symptoms}

Return ONLY valid JSON.

JSON Format:

{{
  "emergency_level": "Low | Moderate | High | Critical",
  "possible_condition": "",
  "immediate_guidance": [
    ""
  ],
  "call_ambulance": false,
  "recommended_department": "",
  "disclaimer": "This is not a medical diagnosis. Seek professional medical care."
}}

Rules:
- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Do NOT explain anything.
"""

    response = generate_response(prompt)

    # Handle both AIMessage and string responses
    if hasattr(response, "content"):
        text = response.content
    else:
        text = str(response)

    print("\n========== RAW GROQ RESPONSE ==========")
    print(text)
    print("=======================================\n")

    # Remove markdown if Groq returns it
    text = re.sub(r"^```json\s*", "", text.strip(), flags=re.IGNORECASE)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    text = text.strip()

    try:
        return json.loads(text)

    except Exception as e:

        print("JSON PARSE ERROR:", e)
        print("RAW TEXT:", text)

        return {
            "emergency_level": "Unknown",
            "possible_condition": "",
            "immediate_guidance": [],
            "call_ambulance": False,
            "recommended_department": "",
            "disclaimer": f"Unable to process response: {e}"
        }