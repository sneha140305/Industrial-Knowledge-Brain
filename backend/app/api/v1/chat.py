from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.get("/")
async def chat_status():
    return {
        "message": "Chat API is under development"
    }