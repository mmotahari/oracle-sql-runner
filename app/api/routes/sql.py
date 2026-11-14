from fastapi import APIRouter, HTTPException

from app.schemas.sql import (
    SQLExecutionRequest,
    SQLExecutionResponse,
)


router = APIRouter(
    prefix="/api/v1/sql",
    tags=["SQL"],
)


@router.post(
    "/execute",
    response_model=SQLExecutionResponse,
)
def execute_sql(request: SQLExecutionRequest):
    raise HTTPException(
        status_code=501,
        detail="SQL execution engine is not implemented yet",
    )