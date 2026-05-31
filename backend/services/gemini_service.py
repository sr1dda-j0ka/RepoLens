import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def ask_gemini(context, question):

    prompt = f"""
You are a senior software engineer.

Answer ONLY using the provided code context.

Rules:
- Mention relevant file paths.
- Explain concepts clearly.
- Do not dump raw code.
- If the answer cannot be found in the context, say so.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text