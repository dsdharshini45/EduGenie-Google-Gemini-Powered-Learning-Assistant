from google import genai

client = genai.Client()


def summarize_text(text):
    prompt = f"""
Summarize the following text in simple language for a student.

Text:
{text}

Give the main points clearly and briefly.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text