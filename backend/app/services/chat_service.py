from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store
from app.services.gemini_service import gemini_service


class ChatService:

    def ask(self, question: str):

        # Create embedding for the user's question
        query_embedding = embedding_service.create_embedding(question)

        # Retrieve similar chunks
        results = vector_store.search(query_embedding)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = "\n\n".join(documents)

        prompt = f"""
You are an Industrial Knowledge Assistant.

Answer ONLY using the information provided below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, reply:
'I couldn't find that information in the uploaded documents.'
"""

        answer = gemini_service.generate_response(prompt)
        
        formatted_sources = []

        for source in metadatas:
            formatted_sources.append(
                {
                     "document": source["filename"],
                     "chunk": source["chunk"]
                }
        )

        return {
            "success": True,
            "answer": answer,
            "sources": formatted_sources
        }
       


chat_service = ChatService()