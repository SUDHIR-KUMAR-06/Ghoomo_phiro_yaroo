from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_landing_page_payload() -> None:
    response = client.get("/api/v1/landing-page")
    assert response.status_code == 200
    payload = response.json()
    assert payload["hero"]["title"] == "Adventure Begins Here."
    assert len(payload["featured_treks"]) == 4


def test_trek_listing() -> None:
    response = client.get("/api/v1/treks")
    assert response.status_code == 200
    payload = response.json()
    assert payload["pagination"]["total"] >= 4
    assert payload["items"][0]["slug"] == "yulakanda-trek"


def test_create_inquiry() -> None:
    response = client.post(
        "/api/v1/inquiries/trek",
        json={
            "name": "Aman Verma",
            "email": "aman@example.com",
            "phone": "+919999999999",
            "trek_id": "trek-1",
            "departure_id": "dep-1",
            "message": "Interested in the June batch",
            "source": "featured_trek_card",
        },
    )
    assert response.status_code == 201
    assert response.json()["status"] == "received"
