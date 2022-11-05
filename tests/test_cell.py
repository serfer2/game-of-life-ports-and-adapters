from hamcrest import assert_that, equal_to

from app.cell import State

from .builders import CellBuilder


class TestCell:
    def test_a_cell_can_die(self):
        cell = CellBuilder().alive().build()

        cell.die()

        assert_that(cell.state, equal_to(State.DEAD))

    def test_a_cell_can_become_alive(self):
        cell = CellBuilder().dead().build()

        cell.revive()

        assert_that(cell.state, equal_to(State.ALIVE))
