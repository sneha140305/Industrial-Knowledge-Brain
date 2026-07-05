from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store

embedding = embedding_service.create_embedding(
    "What is written in the document?"
)

results = vector_store.search(embedding)

print(results)