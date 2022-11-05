from app.cell import Cell, State


class CellBuilder:
    _state: State | None = None

    def dead(self) -> "CellBuilder":
        self._state = State.DEAD
        return self

    def alive(self) -> "CellBuilder":
        self._state = State.ALIVE
        return self

    def build(self):
        if self._state is None:
            raise ValueError("Undefined state")
        return Cell(self._state)
