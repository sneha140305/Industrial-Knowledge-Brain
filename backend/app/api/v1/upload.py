from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.config import settings
from app.services.rag_service import rag_service

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

UPLOAD_DIR = Path(settings.UPLOAD_DIR)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_pdf(
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = rag_service.index_document(
        filename=file.filename,
        file_path=str(file_path),
    )

    return {
        "success": True,
        "message": "Document indexed successfully.",
        **result,
}

