import pytest
from context_managers.Tx import NewTx, Tx


def test_tx_functionality() -> None:
    with pytest.raises(IndexError):
        with Tx("abara-ka-dabara") as tx:
            tx[1000]


def test_new_tx_no_error() -> None:
    with NewTx() as events:
        print(events)


def test_new_tx_with_error() -> None:
    with pytest.raises(IndexError):
        with NewTx() as events:
            print(events[10])


def test_new_tx_error_swallow() -> None:
    with NewTx(swallow=True) as events:
        print(events[10])
