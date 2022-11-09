from .cell import Cell


class Rule:
    def apply(self, cell: Cell, alive_neighbours: int) -> Cell:
        raise NotImplementedError()
