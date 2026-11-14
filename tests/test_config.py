import pytest
from pydantic import ValidationError

from app.core.config import settings, SQLExecutionSettings


def test_sql_execution_settings():
    assert settings.sql_execution.sqlcl_path == "sql"
    assert settings.sql_execution.timeout_seconds == 300


def test_timeout_must_be_positive():
    with pytest.raises(ValidationError):
        SQLExecutionSettings(
            sqlcl_path="sql",
            timeout_seconds=0,
        )