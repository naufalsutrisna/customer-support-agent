import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator

from app.services.chat_service import process_message

router = APIRouter()
logger = logging.getLogger(__name__)


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Message cannot be empty.")
        return value


class ChatResponse(BaseModel):
    conversation_id: str
    answer: str


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        return process_message(
            message=request.message,
            conversation_id=request.conversation_id,
        )
    except Exception:
        logger.exception("Failed to process chat message.")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your message.",
        )
