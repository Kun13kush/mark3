import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from api.main import app

client = TestClient(app)


@patch("api.main.r")  # <-- IMPORTANT: patch the Redis instance
def test_create_job(mock_redis):
    mock_redis.hset.return_value = True
    mock_redis.lpush.return_value = True

    response = client.post("/jobs")

    assert response.status_code == 200
    assert "job_id" in response.json()


@patch("api.main.r")
def test_get_job_status(mock_redis):
    mock_redis.hget.return_value = b"completed"

    response = client.get("/jobs/test-id")

    assert response.status_code == 200
    assert response.json()["status"] == "completed"


@patch("api.main.r")
def test_invalid_job(mock_redis):
    mock_redis.hget.return_value = None

    response = client.get("/jobs/invalid-id")

    assert response.status_code in [200, 404]