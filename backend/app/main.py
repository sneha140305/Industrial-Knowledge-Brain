from fastapi import FastAPI

from app.api.v1.health import router as health_router

app = FastAPI(
    title="Industrial Knowledge Brain",
    version="1.0.0"
)

app.include_router(health_router)