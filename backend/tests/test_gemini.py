from app.services.gemini_service import gemini_service

print(
    gemini_service.generate_response(
        "Say hello."
    )
)