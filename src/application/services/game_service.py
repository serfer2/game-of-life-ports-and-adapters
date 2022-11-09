from typing import Type

from ...domain.models import Space
from ...domain.services import NextState
from ..rules import RULES, Rule
from ..schemas import SpaceSchema


class GameService:
    def __init__(self, rules: list[Type[Rule]] = RULES):
        self._rules = rules

    def play(self, space: SpaceSchema) -> SpaceSchema:
        _space = Space().from_cell_states(states=space.states)
        new_states = NextState().get(space=_space, rules=self._rules)

        return SpaceSchema(states=new_states)
