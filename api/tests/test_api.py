from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import api.main as main


client = TestClient(main.app)


# -------------------------
# MOCK REDIS
# -------------------------
main.r = MagicMock()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_job():
    response = client.post("/jobs")

    assert response.status_code == 200
    data = response.json()

    assert "job_id" in data

    # verify Redis calls
    main.r.lpush.assert_called_once()
    main.r.hset.assert_called_once()


def test_get_job_found():
    main.r.hget.return_value = "completed"

    response = client.get("/jobs/test-id")

    assert response.status_code == 200
    assert response.json()["status"] == "completed"
