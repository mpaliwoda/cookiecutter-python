import pytest


@pytest.mark.parametrize(
    "name,expected_message", [(None, "Hello world"), ("duck", "Hello duck")]
)
def test_{{cookiecutter.project_slug}}_returns_correct_response_based_on_params(
    test_client,
    name,
    expected_message,
):
    path = "/api/v1/{{cookiecutter.project_slug}}"
    if name:
        path += f"?name={name}"

    response = test_client.get(path)

    assert response.status_code == 200
    assert response.json == {"message": expected_message}


def test_{{cookiecutter.project_slug}}_returns_400_on_validation_error(test_client):
    response = test_client.get("/api/v1/{{cookiecutter.project_slug}}?duck=name")

    assert response.status_code == 400
    assert response.json == {
        "validation_error": {
            "query_params": [
                {
                    "loc": ["duck"],
                    "msg": "extra fields not permitted",
                    "type": "value_error.extra",
                }
            ]
        }
    }
