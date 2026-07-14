from pydantic import BaseModel


class ComparisonRequest(BaseModel):
    document1: str
    document2: str


class ComparisonResponse(BaseModel):
    summary: str
    similarities: list[str]
    differences: list[str]
    recommendations: list[str]