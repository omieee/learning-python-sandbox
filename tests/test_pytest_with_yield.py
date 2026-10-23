import pytest


@pytest.fixture
def numbers():
    print("SETUP: making the list")
    data = [1, 2, 3]
    yield data
    print("TEARDOWN: clearing the list")
    data.clear()


def test_sum(numbers):
    print("TEST: running")
    assert sum(numbers) == 6
