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
            events[20000]  # THis will fail and trigger the IndexError
    assert 2 == len(events)
    assert events == ["BEGIN", "ROLLBACK"]


def test_new_tx_error_swallow() -> None:
    with NewTx(swallow=True) as events:
        events[20000]  # This will fail but won't trigger IndexError, hence can't catch
    assert 2 == len(events)
    assert events == ["BEGIN", "ROLLBACK"]
