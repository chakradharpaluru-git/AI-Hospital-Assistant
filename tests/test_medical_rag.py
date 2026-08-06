from backend.ai.medical_rag import ask_medical_question


question = "What are the symptoms of diabetes?"


response = ask_medical_question(question)


print(response)