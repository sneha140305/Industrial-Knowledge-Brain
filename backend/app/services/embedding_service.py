from sentence_transformers import SentenceTransformer

from google import genai
from app.core.config import settings

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):

    return model.encode(chunks).tolist()

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class EmbeddingService:

    def create_embedding(self, text: str):

        response = client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )

        return response.embeddings[0].values


embedding_service = EmbeddingService()