from pydantic import BaseModel
from attributes import Attributes


class Ocurrencia(BaseModel):
    type: str
    id: str
    attributes: dict
    links: dict

    class Config:
        allow_population_by_field_name = True
