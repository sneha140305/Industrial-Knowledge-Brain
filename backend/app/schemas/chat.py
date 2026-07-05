from pydantic import BaseModel


class Source(BaseModel):
    document: str
    chunk: int


class ChatResponse(BaseModel):
    success: bool
    answer: str
    sources: list[Source]