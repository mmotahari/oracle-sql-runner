from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.health import router as health_router
from app.api.routes.sql import router as sql_router


app = FastAPI(
    title=settings.app.name,
    version=settings.app.version,
)

app.include_router(health_router)
app.include_router(sql_router)