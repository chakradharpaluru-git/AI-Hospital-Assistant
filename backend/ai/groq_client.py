import os

from groq import Groq

from dotenv import load_dotenv


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


model = "openai/gpt-oss-20b"


def generate_response(prompt):

    response = client.chat.completions.create(

        model=model,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content