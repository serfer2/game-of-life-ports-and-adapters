import pytest
from hamcrest import assert_that, is_

from src.application.rules import (
    DieByOverpopulation,
    DieByUnderpopulation,
    ReviveCell,
    StillAlive,
)
from src.domain.models import CellBuilder


class TestDieByUnderpopulation:

    rule = DieByUnderpopulation()

    def test_a_living_cell_with_lt_two_neighbours_dies(self):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(cell=living_cell, alive_neighbours=1)

        assert_that(next_gen_cell.is_dead, is_(True))

    def test_it_doesnt_affect_to_dead_cells(self):
        dead_cell = CellBuilder().dead().build()

        next_gen_cell = self.rule.apply(cell=dead_cell, alive_neighbours=2)

        assert_that(next_gen_cell, is_(dead_cell))

    @pytest.mark.parametrize("neighbour_count", (2, 3))
    def test_it_doesnt_affect_to_living_cells_with_gte_two_neighbours_count(
        self, neighbour_count: int
    ):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(
            cell=living_cell,
            alive_neighbours=neighbour_count,
        )

        assert_that(next_gen_cell, is_(living_cell))


class TestStillAlive:

    rule = StillAlive()

    @pytest.mark.parametrize("neighbour_count", (2, 3))
    def test_a_living_cell_with_two_or_three_neighbours_stills_alive(
        self, neighbour_count: int
    ):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(
            cell=living_cell,
            alive_neighbours=neighbour_count,
        )

        assert_that(next_gen_cell.is_alive, is_(True))

    def test_it_doesnt_affect_to_dead_cells(self):
        dead_cell = CellBuilder().dead().build()

        next_gen_cell = self.rule.apply(cell=dead_cell, alive_neighbours=2)

        assert_that(next_gen_cell, is_(dead_cell))

    @pytest.mark.parametrize("neighbour_count", (1, 4))
    def test_it_doesnt_affect_to_living_cells_with_other_neighbours_count(
        self, neighbour_count: int
    ):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(
            cell=living_cell,
            alive_neighbours=neighbour_count,
        )

        assert_that(next_gen_cell, is_(living_cell))


class TestDieByOverpopulation:

    rule = DieByOverpopulation()

    def test_a_living_cell_dies_when_neighbours_count_gt_three(self):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(
            cell=living_cell,
            alive_neighbours=4,
        )

        assert_that(next_gen_cell.is_dead, is_(True))

    def test_it_doesnt_affect_dead_cells(self):
        dead_cell = CellBuilder().dead().build()

        next_gen_cell = self.rule.apply(
            cell=dead_cell,
            alive_neighbours=4,
        )

        assert_that(next_gen_cell, is_(dead_cell))

    @pytest.mark.parametrize("neighbour_count", (3, 2))
    def test_it_doesnt_affect_living_cells_with_lte_three_neigbours(
        self, neighbour_count
    ):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(
            cell=living_cell,
            alive_neighbours=neighbour_count,
        )

        assert_that(next_gen_cell, is_(living_cell))


class TestReviveCell:

    rule = ReviveCell()

    def test_a_dead_cell_revives_when_neighbour_count_is_three(self):
        dead_cell = CellBuilder().dead().build()

        next_gen_cell = self.rule.apply(
            cell=dead_cell,
            alive_neighbours=3,
        )

        assert_that(next_gen_cell.is_alive, is_(True))

    @pytest.mark.parametrize("neighbour_count", (3, 2))
    def test_it_doesnt_affect_living_cells(self, neighbour_count):
        living_cell = CellBuilder().alive().build()

        next_gen_cell = self.rule.apply(
            cell=living_cell,
            alive_neighbours=3,
        )

        assert_that(next_gen_cell, is_(living_cell))

    @pytest.mark.parametrize("neighbour_count", (2, 4))
    def test_it_doesnt_affect_dead_cells_with_other_neighbour_count(
        self, neighbour_count
    ):
        dead_cell = CellBuilder().dead().build()

        next_gen_cell = self.rule.apply(
            cell=dead_cell,
            alive_neighbours=neighbour_count,
        )

        assert_that(next_gen_cell, is_(dead_cell))
