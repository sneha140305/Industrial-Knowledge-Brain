from app.services.chat_service import chat_service

result = chat_service.ask(
    "What is this document about?"
)

print(result)