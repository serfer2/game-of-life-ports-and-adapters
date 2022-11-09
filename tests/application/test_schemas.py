from hamcrest import assert_that, has_property

from src.application.schemas import SpaceSchema
from src.domain.models import State


def test_space_schema():
    states = (
        (State.ALIVE, State.ALIVE, State.ALIVE),
        (State.ALIVE, State.DEAD, State.ALIVE),
        (State.ALIVE, State.ALIVE, State.ALIVE),
    )

    schema = SpaceSchema(states=states)

    assert_that(schema, has_property("states"))
