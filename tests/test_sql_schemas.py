import pytest
from pydantic import ValidationError

from app.schemas.sql import (
    SQLExecutionRequest,
    SQLExecutionResponse,
)


def test_valid_sql_request():
    request = SQLExecutionRequest(
        script="SELECT * FROM DUAL;"
    )

    assert request.script == "SELECT * FROM DUAL;"


def test_empty_sql_request():
    with pytest.raises(ValidationError):
        SQLExecutionRequest(script="")


def test_whitespace_sql_request():
    with pytest.raises(ValidationError):
        SQLExecutionRequest(script="   ")


def test_sql_execution_response():
    response = SQLExecutionResponse(
        status="success",
        output="Query executed successfully",
        execution_time=1.25,
    )

    assert response.status == "success"
    assert response.execution_time == 1.25