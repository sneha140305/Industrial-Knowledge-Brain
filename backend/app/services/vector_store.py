import chromadb

from app.core.config import settings

client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_DIR
)

collection = client.get_or_create_collection(
    name="industrial_documents"
)