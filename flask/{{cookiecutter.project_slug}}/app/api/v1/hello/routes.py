from app.api.v1.hello.models import HelloQueryParameters
from app.models.message import Message
from flask_pydantic import validate

from flask import Blueprint

blueprint = Blueprint(name="todo_v1", import_name=__name__)


@blueprint.route("/")
@validate()
def hello(query: HelloQueryParameters) -> Message:
    return Message(message=f"Hello {query.name}")
