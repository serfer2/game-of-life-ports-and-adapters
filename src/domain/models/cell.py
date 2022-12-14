from enum import Enum


class State(Enum):
    DEAD = 0
    ALIVE = 1


class Cell:
    _state: State

    def __init__(self, state: State) -> None:
        self._state = state

    @property
    def state(self) -> State:
        return self._state

    @property
    def is_alive(self) -> bool:
        return self.state == State.ALIVE

    @property
    def is_dead(self) -> bool:
        return self.state == State.DEAD


class CellBuilder:
    _state: State | None = None

    def dead(self) -> "CellBuilder":
        self._state = State.DEAD
        return self

    def alive(self) -> "CellBuilder":
        self._state = State.ALIVE
        return self

    def with_state(self, state: State) -> "CellBuilder":
        self._state = state
        return self

    def build(self) -> Cell:
        if self._state is None:
            raise ValueError("Undefined state")
        return Cell(self._state)
