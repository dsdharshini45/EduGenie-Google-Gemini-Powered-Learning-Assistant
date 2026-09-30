from google import genai
import json

client = genai.Client()


def generate_quiz(topic):
    prompt = f"""
Create a quiz about the following topic.

Topic: {topic}

Create exactly 3 multiple-choice questions.
Each question must have 4 options.

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question here",
    "options": ["A", "B", "C", "D"],
    "answer": "Correct option"
  }}
]
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)