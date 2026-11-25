from fastapi.testclient import TestClient

from src import api


client = TestClient(api.app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_item():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "price": 10.0, "is_offer": False})
    assert response.status_code == 200
    assert response.json() == {"item_name": "Test Item", "price": 10.0}
