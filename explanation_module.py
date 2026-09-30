from google import genai

client = genai.Client()


def explain_topic(topic):
    prompt = f"""
Explain the following topic in simple language for a student.

Topic: {topic}

Give:
1. A simple definition
2. A clear explanation
3. One simple example
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text