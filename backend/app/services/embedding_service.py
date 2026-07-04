from app.services.gemini_service import gemini_service


class EmbeddingService:
    """
    Creates embeddings using Gemini.
    """

    def create_embedding(
        self,
        text: str,
    ) -> list[float]:

        return gemini_service.get_embedding(text)


embedding_service = EmbeddingService()