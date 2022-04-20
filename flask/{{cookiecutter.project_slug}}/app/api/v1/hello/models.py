from pydantic import BaseModel


class HelloQueryParameters(BaseModel):
    name: str = "world"
