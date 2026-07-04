from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Industrial Knowledge Brain"
    VERSION: str = "1.0.0"

    GEMINI_API_KEY: str = ""

    UPLOAD_DIR: str = "uploads"

    CHROMA_DB_DIR: str = "chroma_db"

    class Config:
        env_file = ".env"


settings = Settings()