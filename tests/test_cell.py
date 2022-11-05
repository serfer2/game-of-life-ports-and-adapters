import pytest
from hamcrest import assert_that, equal_to, is_

from app.cell import CellBuilder, State


class TestCellBuilder:
    def test_build_a_living_cell(self):
        expected_state = State.ALIVE

        cell = CellBuilder().alive().build()

        assert_that(cell.state, equal_to(expected_state))

    def test_build_a_dead_cell(self):
        expected_state = State.DEAD

        cell = CellBuilder().dead().build()

        assert_that(cell.state, equal_to(expected_state))

    def test_a_state_is_needed(self):
        with pytest.raises(ValueError) as excinf:
            CellBuilder().build()

        assert_that(str(excinf.value), equal_to("Undefined state"))


class TestCell:
    def test_living_cell_is_alive_is_True(self):
        cell = CellBuilder().alive().build()

        assert_that(cell.is_alive, is_(True))

    def test_dead_cell_is_alive_is_False(self):
        cell = CellBuilder().dead().build()

        assert_that(cell.is_alive, is_(False))

    def test_dead_cell_is_dead_is_True(self):
        cell = CellBuilder().dead().build()

        assert_that(cell.is_dead, is_(True))

    def test_living_cell_is_dead_is_False(self):
        cell = CellBuilder().alive().build()

        assert_that(cell.is_dead, is_(False))
