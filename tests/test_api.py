from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "This is a test",
        "done": False
    })
    assert response.status_code == 200

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_delete_task():
    # First create a task
    create = client.post("/tasks", json={"title": "To Delete"})
    task_id = create.json()["task"]["id"]
    # Then delete it
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

