from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_valid_date():
    response = client.get("/api/16-03-2023")
    assert response.status_code == 200
    assert response.json() == {"dia": "16-03-2023", "valor": "28210.24"}

def test_invalid_date_format():
    response = client.get("/api/2023-03-16")
    assert response.status_code == 422
    assert response.json() == {"detail": [{"loc": ["path", "date"], "msg": "value is not a valid datetime", "type": "type_error.datetime"}]}

def test_invalid_date():
    response = client.get("/api/31-04-2023")
    assert response.status_code == 404
    assert response.json() == {"error": "Date not available"}

def test_date_before_2013():
    response = client.get("/api/31-12-2012")
    assert response.status_code == 404
    assert response.json() == {"error": "Date not available (< 2013)"}