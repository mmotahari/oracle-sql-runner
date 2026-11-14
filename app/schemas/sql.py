from typing import Literal

from pydantic import BaseModel, Field, field_validator


class SQLExecutionRequest(BaseModel):
    script: str = Field(
        min_length=1,
        description="SQL script to execute"
    )

    @field_validator("script")
    @classmethod
    def validate_script(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("SQL script cannot be empty")

        return value


class SQLExecutionResponse(BaseModel):
    status: Literal["success", "error"]
    output: str = ""
    error: str | None = None
    execution_time: float | None = None