from app.services.pdf_service import pdf_service
from app.services.chunk_service import chunk_service
from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store
from app.services.entity_service import entity_service


class RAGService:
    """
    Handles complete document indexing.
    """

    def index_document(
        self,
        filename: str,
        file_path: str,
    ) -> dict:

        # -----------------------------------
        # Extract Text
        # -----------------------------------

        text = pdf_service.extract_text(file_path)

        # -----------------------------------
        # Extract Entities
        # -----------------------------------

        entities = entity_service.extract_entities(text)

        # -----------------------------------
        # Split into Chunks
        # -----------------------------------

        chunks = chunk_service.chunk_text(text)

        # -----------------------------------
        # Create Full Document Embedding
        # -----------------------------------

        document_embedding = embedding_service.create_embedding(text)

        # -----------------------------------
        # Find Similar Documents
        # -----------------------------------

        similar_documents = vector_store.similar_documents(
            document_embedding,
            filename
        )

        # -----------------------------------
        # Store Chunks
        # -----------------------------------

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

        # -----------------------------------
        # Return Upload Result
        # -----------------------------------

        return {
            "filename": filename,
            "chunks": len(chunks),
            "entities": entities,
            "similar_documents": similar_documents
        }


rag_service = RAGService()