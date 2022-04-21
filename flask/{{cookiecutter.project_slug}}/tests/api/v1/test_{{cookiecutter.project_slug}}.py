def test_{{cookiecutter.project_slug}}_returns_default_greeting_when_no_params_provided(test_client):
    response = test_client.get("/api/v1/{{cookiecutter.project_slug}}")

    assert response.status_code == 200
    assert response.json == {"message": "Hello world"}
