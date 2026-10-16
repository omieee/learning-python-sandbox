import pytest
from context_managers.Tx import NewTx, Tx


def test_tx_functionality() -> None:
    with pytest.raises(IndexError):
        with Tx("abara-ka-dabara") as tx:
            tx[1000]


def test_new_tx_no_error() -> None:
    with NewTx() as events:
        assert events == ["BEGIN"]
        assert 1 == len(events)  # Till now it has not exited so only "BEGIN" is there
    assert 2 == len(events)  # Now exited and __exit__ got executed
    assert events == ["BEGIN", "COMMIT"]


def test_new_tx_with_error() -> None:
    with pytest.raises(IndexError):
        with NewTx() as events:
            print(events[20000])
            assert events == ["BEG"]  # you need to fix this, looks wrong to me


def test_new_tx_error_swallow() -> None:
    with NewTx(swallow=True) as events:
        assert events == ["BEGIN"]
        assert 1 == len(events)
    assert events == ["BEGIN", "COMMIT"]
