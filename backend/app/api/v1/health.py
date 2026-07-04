from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health():
    return {
        "status": "Running",
        "message": "Industrial Knowledge Brain API is healthy.",
    }