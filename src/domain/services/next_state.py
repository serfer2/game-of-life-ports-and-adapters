from typing import Type

from ..models import Rule, Space, State


class NextState:
    def get(self, space: Space, rules: list[Type[Rule]]) -> list[list[State]]:
        new_states = []
        for posy, row in enumerate(space):
            new_states_row = []
            for posx, cell in enumerate(row):
                alive = space.count_cell_alive_neighbours(posx=posx, posy=posy)

                for rule in rules:
                    cell = rule().apply(cell=cell, alive_neighbours=alive)

                new_states_row.append(cell.state)

            new_states.append(new_states_row)

        return new_states
