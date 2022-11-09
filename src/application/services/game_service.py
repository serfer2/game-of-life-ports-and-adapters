from typing import Type

from ...domain.models import Space
from ..rules import RULES, Rule
from ..schemas import SpaceSchema


class GameService:
    def __init__(self, rules: list[Type[Rule]] = RULES):
        self._rules = rules

    def play(self, space: SpaceSchema) -> SpaceSchema:
        _space = Space().from_cell_states(states=space.states)
        new_states = []
        for posy, row in enumerate(_space):
            new_states_row = []
            for posx, cell in enumerate(row):
                alive = _space.count_cell_alive_neighbours(posx=posx, posy=posy)

                for rule in RULES:
                    cell = rule().apply(cell=cell, alive_neighbours=alive)

                new_states_row.append(cell.state)

            new_states.append(new_states_row)

        return SpaceSchema(states=new_states)
