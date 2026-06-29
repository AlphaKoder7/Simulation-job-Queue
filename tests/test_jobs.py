from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_job():
    response = client.post("/jobs", json={"type": "wind_analysis"})
    assert response.status_code == 201
    data = response.json()
    assert data["type"] == "wind_analysis"
    assert data["status"] == "PENDING"
    assert "id" in data
    assert "created_at" in data


def test_get_job():
    create = client.post("/jobs", json={"type": "stress_test"})
    job_id = create.json()["id"]

    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["id"] == job_id


def test_get_job_not_found():
    response = client.get("/jobs/00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404


def test_list_jobs():
    client.post("/jobs", json={"type": "wind_analysis"})
    response = client.get("/jobs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0