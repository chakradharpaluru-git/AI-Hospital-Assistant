import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def summarize_report(text):

    prompt = f"""
    Analyze this medical report.

    Provide:

    1. Medical Report Summary
    2. Possible Diagnosis
    3. Medicines Mentioned
    4. Recommendations


    Medical Report:

    {text}
    """


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a medical assistant AI. Provide clear structured analysis."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )


    return response.choices[0].message.content