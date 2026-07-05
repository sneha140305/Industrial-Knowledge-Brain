from pydantic import BaseModel
from fastapi import APIRouter

from app.services.chat_service import chat_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
async def chat(request: ChatRequest):
    return chat_service.ask(request.question)