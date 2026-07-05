import chromadb

from app.core.config import settings


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_DIR
        )

        self.collection = self.client.get_or_create_collection(
            name="industrial_documents"
        )

    def add_document(
        self,
        doc_id: str,
        chunk: str,
        embedding: list[float],
        metadata: dict,
    ):
        self.collection.add(
            ids=[doc_id],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[metadata],
        )

    def search(
        self,
        embedding: list[float],
        n_results: int = 5,
    ):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )
    
    def delete_document(self, doc_id: str):
        results = self.collection.get(
            where={
            "filename": filename
            }
        )
        ids = results.get("ids", [])

        if ids:
           self.collection.delete(ids=ids)

        return len(ids)
    
    def get_stats(self):
        return{
            "chunks": self.collection.count()
        }
vector_store = VectorStore()