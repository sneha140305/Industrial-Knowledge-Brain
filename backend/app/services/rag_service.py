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

        print("=" * 60)
        print("Starting document indexing...")
        print(f"File: {filename}")

        # -----------------------------------
        # Extract Text
        # -----------------------------------

        print("STEP 1 - Extracting text...")

        text = pdf_service.extract_text(file_path)

        print(f"✓ Text extracted ({len(text)} characters)")

        # -----------------------------------
        # Extract Entities
        # -----------------------------------

        print("STEP 2 - Extracting entities...")

        entities = entity_service.extract_entities(text)

        print(f"✓ Found {len(entities)} entities")

        # -----------------------------------
        # Split into Chunks
        # -----------------------------------

        print("STEP 3 - Chunking document...")

        chunks = chunk_service.chunk_text(text)

        print(f"✓ Created {len(chunks)} chunks")

        # -----------------------------------
        # Create Full Document Embedding
        # -----------------------------------

        print("STEP 4 - Creating document embedding...")

        document_embedding = embedding_service.create_embedding(text)

        print("✓ Document embedding created")

        # -----------------------------------
        # Find Similar Documents
        # -----------------------------------

        print("STEP 5 - Searching similar documents...")

        similar_documents = vector_store.similar_documents(
            document_embedding,
            filename
        )

        print(f"✓ Found {len(similar_documents)} similar documents")

        # -----------------------------------
        # Store Chunks
        # -----------------------------------

        print("STEP 6 - Storing chunks...")

        for index, chunk in enumerate(chunks):

            print(f"  Processing chunk {index + 1}/{len(chunks)}")

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

        print("✓ All chunks stored successfully")
        print("Document indexing completed")
        print("=" * 60)

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