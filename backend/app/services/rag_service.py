from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store


class RAGService:

    def index_document(
        self,
        filename: str,
        text: str
    ):

        chunks = chunk_service.chunk_text(text)

        for i, chunk in enumerate(chunks):

            embedding = embedding_service.create_embedding(chunk)

            vector_store.add_document(
                doc_id=f"{filename}_{i}",
                chunk=chunk,
                embedding=embedding,
                metadata={
                    "filename": filename,
                    "chunk": i
                }
            )

        return len(chunks)


rag_service = RAGService()