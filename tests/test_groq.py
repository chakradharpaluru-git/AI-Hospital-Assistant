from backend.ai.groq_client import generate_response


answer = generate_response(
    "Explain the symptoms of pneumonia"
)


print(answer)