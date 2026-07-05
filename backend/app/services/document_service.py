import os
from app.core.config import settings
from app.services.vector_store import vector_store

class DocumentService:

    def list_documents(self):
        documents = []

        if not os.path.exists(settings.UPLOAD_DIR):
            return documents

        for filename in os.listdir(settings.UPLOAD_DIR):

            if filename.endswith(".pdf"):

                documents.append({
                    "filename": filename
                })

        return documents

    def delete_document(self, filename: str):

      file_path = os.path.join(
        settings.UPLOAD_DIR,
        filename
      )

      if not os.path.exists(file_path):
        return None
      
      deleted_chunks = vector_store.delete_document(filename)
      os.remove(file_path)

      return {
         "filename": filename,
         "deleted_chunks": deleted_chunks
    }

    
    def get_dashboard_stats(self):

       documents = self.list_documents()

       return {
          "documents": len(documents),
          "chunks": vector_store.get_stats()["chunks"],
        "backend": "Online"
    }


document_service = DocumentService()