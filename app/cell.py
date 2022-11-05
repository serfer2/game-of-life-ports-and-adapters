from enum import Enum


class State(Enum):
    ALIVE = 0
    DEAD = 1


class Cell:
    _state: State | None = None

    def __init__(self, state: State) -> None:
        self._state = state

    @property
    def state(self) -> State:
        return self._state

    def die(self):
        self._state = State.DEAD

    def revive(self):
        self._state = State.ALIVE
