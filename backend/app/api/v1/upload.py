from fastapi import APIRouter

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.get("/")
async def upload_status():
    return {
        "message": "Upload API is under development"
    }

