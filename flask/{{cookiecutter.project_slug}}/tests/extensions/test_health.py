from unittest.mock import ANY, patch

from app.extensions.health import health_check


def test_returns_healthy_response_if_service_is_up(test_client):
    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json["message"] == "success"
    assert response.json["results"] == [
        {
            "checker": "check_service",
            "output": "service ok",
            "passed": True,
            "timestamp": ANY,
            "expires": ANY,
            "response_time": ANY,
        }
    ]


def test_returns_not_healthy_response_if_service_is_down(test_client):
    def check_service():
        return False, "service down"

    with patch.object(health_check, "checkers", [check_service]):
        response = test_client.get("/health")

    assert response.status_code == 500
    assert response.json["message"] == "failure"
    assert response.json["results"] == [
        {
            "checker": "check_service",
            "output": "service down",
            "passed": False,
            "timestamp": ANY,
            "expires": ANY,
            "response_time": ANY,
        }
    ]
