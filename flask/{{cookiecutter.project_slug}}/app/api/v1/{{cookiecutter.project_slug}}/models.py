from pydantic import BaseModel, Extra


class HelloQueryParameters(BaseModel, extra=Extra.forbid):
    name: str = "world"
