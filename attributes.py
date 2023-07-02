from pydantic import BaseModel


class Attributes(BaseModel):
    id: str
    self: str
    name: str
    dateFull: dict
    date_start: str
    date_end: str
    text: str
    ticket: str
    ticket_value: str
    eventual_name: str
    eventual_direccion: str
    eventual_coords: str
    eventual_distrito: str
    suspendida: bool
    status: str
    actividad: str
    regla: str
    regla_er: str