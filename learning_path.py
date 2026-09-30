from google import genai

client = genai.Client()


def recommend_learning_path(topic):
    prompt = f"""
Create a learning path for a student who wants to learn:

Topic: {topic}

Organize the learning path from beginner to advanced.

For each stage, include:
1. Topic to learn
2. Difficulty level
3. A short description
4. Suggested learning resources
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text