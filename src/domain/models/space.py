from collections.abc import Sequence
from typing import Iterable

from .cell import Cell, CellBuilder, State


class Space:
    _cells: Iterable[Iterable[Cell]] = [[]]

    def __iter__(self):
        return self._cells.__iter__()

    @property
    def dimensions(self):
        # 2D: height, width
        return (len(self._cells), len(self._cells[0]))

    def from_cell_states(self, states: Sequence[Sequence[State]]) -> "Space":
        if (
            not states
            or type(states) not in (list, tuple)  # noqa: W503
            or type(states[0]) not in (list, tuple)  # noqa: W503
        ):
            raise ValueError("States should be a 2 dim iterable")
        row_lengths = set([sum(1 for _ in row) for row in states])
        if len(row_lengths) != 1:
            raise ValueError("Rows must have same length")

        self._cells = []

        for row in states:
            new_row = []
            for state in row:
                new_row.append(CellBuilder().with_state(state).build())
            self._cells.append(new_row)

        return self

    def neighbour_coordinates(
        self, posx: int, posy: int
    ) -> list[tuple[int, int]]:
        coordinates_360 = [
            (posx - 1, posy - 1),
            (posx - 1, posy),
            (posx - 1, posy + 1),
            (posx, posy + 1),
            (posx + 1, posy + 1),
            (posx + 1, posy),
            (posx + 1, posy - 1),
            (posx, posy - 1),
        ]
        neighbour_coordinates = []
        for coordinate in coordinates_360:
            if coordinate[0] >= 0 and coordinate[1] >= 0:
                neighbour_coordinates.append(coordinate)

        return neighbour_coordinates
