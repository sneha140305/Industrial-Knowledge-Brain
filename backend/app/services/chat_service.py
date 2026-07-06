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
        distances = results["distances"][0]

        # Build sources with confidence and evidence
        sources = []

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances
        ):

            # Simple confidence mapping
            if distance < 0.30:
                confidence = 95
            elif distance < 0.50:
                confidence = 85
            elif distance < 0.70:
                confidence = 70
            else:
                confidence = 55

            sources.append(
                {
                    "filename": meta["filename"],
                    "chunk": meta["chunk"],
                    "confidence": confidence,
                    "evidence": doc[:350] + "..."
                }
            )

        # Build context for Gemini
        context = "\n\n".join(documents)

        prompt = f"""
You are an Industrial Knowledge Assistant.

Role:
- Help engineers, technicians, operators, and students understand industrial documents.
- Answer ONLY using the retrieved context.
- Never make up information.
- If the answer is not available, reply:
'I couldn't find that information in the uploaded documents.'

Instructions:
- Be clear and concise.
- Use bullet points whenever appropriate.
- Mention safety precautions if present.
- Explain procedures step by step.
- Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = gemini_service.generate_response(prompt)

        return {
            "success": True,
            "answer": answer,
            "sources": sources
        }

chat_service = ChatService()