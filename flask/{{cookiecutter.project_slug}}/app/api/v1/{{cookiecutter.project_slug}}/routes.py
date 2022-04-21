from app.api.v1.{{cookiecutter.project_slug}}.models import HelloQueryParameters
from app.models.message import Message
from flask_pydantic import validate

from flask import Blueprint

blueprint = Blueprint(name="{{cookiecutter.project_slug}}_v1", import_name=__name__)


@blueprint.route("/", methods=["GET"])
@validate()
def hello(query: HelloQueryParameters) -> Message:
    return Message(message=f"Hello {query.name}")
