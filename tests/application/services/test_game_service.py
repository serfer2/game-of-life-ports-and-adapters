from hamcrest import assert_that, equal_to

from src.application.rules import RULES
from src.application.schemas import SpaceSchema
from src.application.services import GameService


def test_play(iteration_examples):
    service = GameService(rules=RULES)
    for current_space_state, next_space_state in iteration_examples:
        expected_nex_state = SpaceSchema(states=next_space_state)
        current_space_state = SpaceSchema(states=current_space_state)

        new_space_state = service.play(space=current_space_state)

        assert_that(new_space_state, equal_to(expected_nex_state))
