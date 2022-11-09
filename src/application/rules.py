from ..domain.models import Cell, CellBuilder, Rule


class DieByUnderpopulation(Rule):
    """Any live cell with fewer than two live neighbours dies,
    as if by underpopulation.
    """

    def apply(self, cell: Cell, alive_neighbours: int) -> Cell:
        if cell.is_alive and alive_neighbours < 2:
            return CellBuilder().dead().build()
        return cell


class StillAlive(Rule):
    """Any live cell with two or three live neighbours lives on to
    the next generation.
    """

    def apply(self, cell: Cell, alive_neighbours: int) -> Cell:
        if cell.is_alive and alive_neighbours in (2, 3):
            return CellBuilder().alive().build()
        return cell


class DieByOverpopulation(Rule):
    """Any live cell with more than three live neighbours dies,
    as if by overpopulation.
    """

    def apply(self, cell: Cell, alive_neighbours: int) -> Cell:
        if cell.is_alive and alive_neighbours > 3:
            return CellBuilder().dead().build()
        return cell


class ReviveCell(Rule):
    """Any dead cell with exactly three live neighbours becomes a
    live cell, as if by reproduction.
    """

    def apply(self, cell: Cell, alive_neighbours: int) -> Cell:
        if cell.is_dead and alive_neighbours == 3:
            return CellBuilder().alive().build()
        return cell


RULES = [DieByUnderpopulation, StillAlive, DieByOverpopulation, ReviveCell]
