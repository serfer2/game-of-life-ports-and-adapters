import pytest

from src.domain.models import CellBuilder, Rule


class TestRuleBaseClass:
    def test_its_next_gen_method_must_be_overwritten(self):
        cell = CellBuilder().alive().build()

        with pytest.raises(NotImplementedError):
            Rule().apply(cell=cell, alive_neighbours=1)
