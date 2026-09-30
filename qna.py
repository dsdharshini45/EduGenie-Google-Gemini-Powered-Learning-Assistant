from google import genai

client = genai.Client()


def ask_question(question):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question
    )

    return response.text