from fastapi import APIRouter, HTTPException

from app.schemas.comparison import (
    ComparisonRequest,
    ComparisonResponse
)
from app.services.comparison_service import comparison_service

router = APIRouter(
    prefix="/comparison",
    tags=["Document Comparison"]
)


@router.post(
    "/",
    response_model=ComparisonResponse
)
def compare_documents(
    request: ComparisonRequest
):

    try:

        result = comparison_service.compare_documents(
            request.document1,
            request.document2
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )