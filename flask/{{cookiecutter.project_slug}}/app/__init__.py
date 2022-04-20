from app.api.v1 import hello as hello_v1
from app.extensions.health import health_check

from flask import Flask

VERSION = "0.1.0"


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)

    app.testing = testing

    app.register_blueprint(hello_v1.blueprint, url_prefix="/api/v1/hello")
    app.add_url_rule("/health", "healthcheck", view_func=lambda: health_check.run())

    return app


if __name__ == "__main__":
    app = create_app()
