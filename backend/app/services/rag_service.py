from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store


class RAGService:
    """
    Handles complete document indexing.
    """

    def index_document(
        self,
        filename: str,
        file_path: str,
    ) -> dict:

        # Extract text
        text = pdf_service.extract_text(file_path)

        # Split into chunks
        chunks = chunk_service.chunk_text(text)

        # Store each chunk
        for index, chunk in enumerate(chunks):

            embedding = embedding_service.create_embedding(chunk)

            vector_store.add_document(
                doc_id=f"{filename}_{index}",
                chunk=chunk,
                embedding=embedding,
                metadata={
                    "filename": filename,
                    "chunk": index,
                },
            )

        return {
            "filename": filename,
            "chunks": len(chunks),
        }


rag_service = RAGService()