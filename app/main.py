from fastapi import FastAPI

from app.core.config import settings

app=FastAPI(
    title=settings.app.name,
    version=settings.app.version,
)

@app.get("/health")
def health_check():
    return {
    "status": "ok",
    "application": settings.app.name,
    "version": settings.app.version,
}
