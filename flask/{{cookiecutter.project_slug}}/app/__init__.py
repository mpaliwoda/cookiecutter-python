from app.api.v1 import {{cookiecutter.project_slug}} as {{cookiecutter.project_slug}}_v1
from app.extensions.health import health_check

from flask import Flask

VERSION = "0.1.0"


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)

    app.testing = testing

    app.url_map.strict_slashes = False

    app.add_url_rule("/health", "healthcheck", view_func=lambda: health_check.run())
    app.register_blueprint({{cookiecutter.project_slug}}_v1.blueprint, url_prefix="/api/v1/{{cookiecutter.project_slug}}")

    return app


if __name__ == "__main__":
    app = create_app()
