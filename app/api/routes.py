from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import process_message

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = process_message(request.message)

    return {"answer": answer}
