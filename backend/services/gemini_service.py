import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def ask_gemini(context, question):

    prompt = f"""
You are a senior software engineer analyzing a codebase.

You MUST answer only from the provided context.

Rules:
- Mention file paths whenever possible.
- Explain the implementation in plain English.
- Do not invent functionality.
- Do not use outside knowledge.
- If the context is insufficient, reply exactly:

"Information not found in the retrieved code context."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt,
            config={
                "temperature" : 0.1,
                "max_output_tokens" : 500
            }
        )
        return response.text
    
    except Exception as e:
        return f"Gemini Error: {str(e)}"