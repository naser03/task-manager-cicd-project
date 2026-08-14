import pytest
from app import app, tasks


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear()
    tasks.extend([
        {"id": 1, "title": "Test task", "completed": False}
    ])


def test_health(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_get_tasks(client):
    response = client.get("/api/tasks")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={"title": "Learn GitHub Actions"}
    )

    assert response.status_code == 201
    assert response.json["title"] == "Learn GitHub Actions"
    assert response.json["completed"] is False


def test_empty_task_rejected(client):
    response = client.post(
        "/api/tasks",
        json={"title": ""}
    )

    assert response.status_code == 400


def test_toggle_task(client):
    response = client.patch("/api/tasks/1")

    assert response.status_code == 200
    assert response.json["completed"] is True


def test_delete_task(client):
    response = client.delete("/api/tasks/1")

    assert response.status_code == 200
    assert len(tasks) == 0


def test_missing_task(client):
    response = client.patch("/api/tasks/999")

    assert response.status_code == 404
