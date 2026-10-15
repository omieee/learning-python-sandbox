import pytest
from context_managers.Tx import Tx


def test_tx_functionality() -> None:
    with pytest.raises(IndexError):
        with Tx("abara-ka-dabara") as tx:
            tx[1000]
