from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import process_message

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return process_message(
        message=request.message,
        conversation_id=request.conversation_id,
    )
