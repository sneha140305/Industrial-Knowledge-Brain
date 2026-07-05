from fastapi import APIRouter, HTTPException

from app.services.document_service import document_service
from app.services.vector_store import vector_store

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/")
def get_documents():
    return document_service.list_documents()


@router.delete("/{filename}")
def delete_document(filename: str):

    result = document_service.delete_document(filename)

    if result:

        return {
            "success": True,
            "message": "Document deleted successfully.",
            **result
        }

    raise HTTPException(
        status_code=404,
        detail="Document not found."
    )

@router.get("/stats")
def stats():

    return vector_store.get_stats()

@router.get("/dashboard")
def dashboard():

    return document_service.get_dashboard_stats()