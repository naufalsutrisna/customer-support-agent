
from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import graph

app = FastAPI(title="Customer Support Agent")


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = graph.invoke(
        {
            "messages": [
                {"role": "user", "content": request.message}
            ]
        }
    )

    answer = result["messages"][-1].content

    return {"answer": answer}
