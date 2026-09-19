from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Orchestration API")


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "FastAPI is running successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


@app.post("/chat")
def chat(data: Question):

    answer = f"You asked: {data.question}"

    return {
        "question": data.question,
        "answer": answer
    }