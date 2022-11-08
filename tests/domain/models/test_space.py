import pytest
from hamcrest import assert_that, equal_to, has_items

from src.domain.models import Space, State


class TestSpace:
    def test_it_raises_exception_when_rows_have_different_length(self):
        states = (
            (State.ALIVE, State.ALIVE, State.ALIVE),
            (State.ALIVE, State.ALIVE, State.ALIVE, State.ALIVE),
            (State.ALIVE, State.ALIVE, State.ALIVE),
        )
        expected_error_msg = "Rows must have same length"

        with pytest.raises(ValueError) as excinf:
            Space().from_cell_states(states=states)

        assert_that(str(excinf.value), equal_to(expected_error_msg))

    def test_it_raises_exception_when_states_is_empty(self):
        states = []
        expected_error_msg = "States should be a 2 dim iterable"

        with pytest.raises(ValueError) as excinf:
            Space().from_cell_states(states=states)

        assert_that(str(excinf.value), equal_to(expected_error_msg))

    def test_it_returns_a_new_cells_space_with_same_states(self):
        states = (
            (State.ALIVE, State.DEAD, State.ALIVE),
            (State.ALIVE, State.DEAD, State.ALIVE),
            (State.ALIVE, State.DEAD, State.ALIVE),
        )

        space = Space().from_cell_states(states=states)

        for i, row in enumerate(space):
            for j, cell in enumerate(row):
                assert_that(cell.state, equal_to(states[i][j]))

    def test_it_returns_its_dimensions(self):
        space = Space()

        assert_that(space.dimensions, equal_to((1, 0)))


class TestNeighboursCoordinates:
    states = (
        (State.ALIVE, State.DEAD, State.ALIVE),
        (State.ALIVE, State.DEAD, State.ALIVE),
        (State.ALIVE, State.DEAD, State.ALIVE),
    )
    space = Space().from_cell_states(states=states)

    def test_centered_cell(self):
        x = 1
        y = 1
        expected_neighbour_coord = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (2, 1),
            (2, 0),
            (1, 0),
        ]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_top_left(self):
        x = 0
        y = 0
        expected_neighbour_coord = [(0, 1), (1, 1), (1, 0)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_top_center(self):
        x = 1
        y = 0
        expected_neighbour_coord = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_top_right(self):
        x = 2
        y = 0
        expected_neighbour_coord = [(1, 0), (1, 1), (2, 1)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_left_center(self):
        x = 0
        y = 1
        expected_neighbour_coord = [(0, 2), (1, 2), (1, 1), (1, 0), (0, 0)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_bottom_left(self):
        x = 0
        y = 2
        expected_neighbour_coord = [(1, 2), (1, 1), (0, 1)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_bottom_center(self):
        x = 1
        y = 2
        expected_neighbour_coord = [(0, 1), (0, 2), (2, 2), (2, 1), (1, 1)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_bottom_right(self):
        x = 2
        y = 2
        expected_neighbour_coord = [(1, 1), (2, 1), (2, 1)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))

    def test_right_center(self):
        x = 2
        y = 1
        expected_neighbour_coord = [(1, 0), (1, 1), (1, 2), (2, 2), (2, 0)]

        neighbours = self.space.neighbour_coordinates(posx=x, posy=y)

        assert_that(neighbours, has_items(*expected_neighbour_coord))
