from typing import List


class ChunkService:
    """
    Splits long text into overlapping chunks.
    """

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 500,
        overlap: int = 100,
    ) -> List[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append(text[start:end])

            start += chunk_size - overlap

        return chunks


chunk_service = ChunkService()