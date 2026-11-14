from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_execute_sql_not_implemented_yet():
    response = client.post(
        "/api/v1/sql/execute",
        json={"script": "SELECT * FROM employees;"},
    )

    assert response.status_code == 501
    assert response.json() == {
        "detail": "SQL execution engine is not implemented yet"
    }


def test_execute_sql_with_empty_script():
    response = client.post(
        "/api/v1/sql/execute",
        json={"script": ""},
    )

    assert response.status_code == 422