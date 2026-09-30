from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import ask_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/qa")
def qa(question: str):
    answer = ask_question(question)
    return {"question": question, "answer": answer}


@app.get("/explain")
def explain(topic: str):
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


@app.get("/quiz")
def quiz(topic: str):
    questions = generate_quiz(topic)
    return {"topic": topic, "quiz": questions}


@app.get("/summarize")
def summarize(text: str):
    summary = summarize_text(text)
    return {"text": text, "summary": summary}


@app.get("/learn/recommendations")
def learning_recommendations(topic: str):
    recommendations = recommend_learning_path(topic)
    return {"topic": topic, "recommendations": recommendations}