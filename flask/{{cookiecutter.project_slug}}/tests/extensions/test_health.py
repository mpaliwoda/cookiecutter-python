from unittest.mock import ANY


def test_returns_healthy_response_if_service_is_up(test_client):
    response = test_client.get("/health")

    assert response.status_code == 200
    assert response.json["message"] == "success"
    assert response.json["results"] == [
        {
            "checker": "check_service",
            "output": "Service ok",
            "passed": True,
            "timestamp": ANY,
            "expires": ANY,
            "response_time": ANY,
        }
    ]
