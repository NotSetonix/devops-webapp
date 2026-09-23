import pytest
from app import app, tasks

@pytest.fixture
def client():
    app.config["TESTING"] = True
    tasks.clear()
    return app.test_client()

def test_home_page(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"DevOps Task List" in r.data

def test_health(client):
    r = client.get("/health")
    assert r.json == {"status": "ok"}

def test_add_task(client):
    client.post("/", data={"task": "Learn Docker"})
    r = client.get("/")
    assert b"Learn Docker" in r.data
