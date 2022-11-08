from .cell import Cell, CellBuilder


class Rule:
    def next_gen(self, cell: Cell, neighbour_count: int) -> Cell:
        raise NotImplementedError()


class DieByUnderpopulation(Rule):
    """Any live cell with fewer than two live neighbours dies,
    as if by underpopulation.
    """

    def next_gen(self, cell: Cell, neighbour_count: int) -> Cell:
        if cell.is_alive and neighbour_count < 2:
            return CellBuilder().dead().build()
        return cell


class StillAlive(Rule):
    """Any live cell with two or three live neighbours lives on to
    the next generation.
    """

    def next_gen(self, cell: Cell, neighbour_count: int) -> Cell:
        if cell.is_alive and neighbour_count in (2, 3):
            return CellBuilder().alive().build()
        return cell


class DieByOverpopulation(Rule):
    """Any live cell with more than three live neighbours dies,
    as if by overpopulation.
    """

    def next_gen(self, cell: Cell, neighbour_count: int) -> Cell:
        if cell.is_alive and neighbour_count > 3:
            return CellBuilder().dead().build()
        return cell


class ReviveCell(Rule):
    """Any dead cell with exactly three live neighbours becomes a
    live cell, as if by reproduction.
    """

    def next_gen(self, cell: Cell, neighbour_count: int) -> Cell:
        if cell.is_dead and neighbour_count == 3:
            return CellBuilder().alive().build()
        return cell


RULES = (DieByUnderpopulation, StillAlive, DieByOverpopulation, ReviveCell)
