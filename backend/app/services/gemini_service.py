from google import genai

from app.core.config import settings


class GeminiService:
    """
    Handles all communication with Google's Gemini API.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def get_embedding(self, text: str) -> list[float]:
        response = self.client.models.embed_content(
            model="gemini-embedding-001",
            contents=text,
        )

        return response.embeddings[0].values

    def generate_response(
        self,
        prompt: str,
    ) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text


gemini_service = GeminiService()