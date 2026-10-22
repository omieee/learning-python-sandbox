import pytest
from context_managers.Tx import NewTx


@pytest.fixture
def evnt():
    with NewTx() as events:
        yield events
    print("\nafter:", events)


@pytest.fixture
def rollback_events():
    with pytest.raises(IndexError):
        with NewTx() as events:
            yield events
        print("\nafter:", events)


def test_newtx_pass(evnt):
    evnt.append("INSERT")
    assert evnt == ["BEGIN", "INSERT"]


# @pytest.mark.xfail(strict=True)
# def test_newtx_insert_fail(evnt):
#     evnt.append("INSERT")
#     assert True


# def test_rollback_events_pass(rollback_events):
#     rollback_events.append("INSERT")
#     rollback_events[20000]
#     assert rollback_events == ["BEGIN", "INSERT", "ROLLBACK"]
