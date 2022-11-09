from pydantic import BaseModel

from ..domain.models import State


class SpaceSchema(BaseModel):
    states: list[list[State]]
