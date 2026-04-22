import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_job_status():
    create = client.post("/jobs").json()
    job_id = create["job_id"]

    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert "status" in response.json()


def test_invalid_job():
    response = client.get("/jobs/invalid-id")
    assert response.status_code in [400, 404]