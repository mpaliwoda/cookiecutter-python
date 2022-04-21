from http import HTTPStatus

from app.api.v1 import {{cookiecutter.project_slug}} as {{cookiecutter.project_slug}}_v1
from app.extensions.health import health_check
from pydantic import ValidationError

from flask import Flask


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)

    app.testing = testing

    app.url_map.strict_slashes = False

    app.add_url_rule("/health", "healthcheck", view_func=lambda: health_check.run())
    app.register_blueprint({{cookiecutter.project_slug}}_v1.blueprint, url_prefix="/api/v1/{{cookiecutter.project_slug}}")

    @app.errorhandler(ValidationError)
    def handle_validation_error(error: ValidationError) -> tuple[str, int]:
        return error.json(), HTTPStatus.BAD_REQUEST

    return app
