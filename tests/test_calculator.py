import pytest
from basic_pytest_learning.calculator import Calculator


@pytest.mark.parametrize(
    "first_num, second_num, expected",
    [(5, 3, 8), (4, 2, 6), (-12, 12, 0), (-12, -13, -25), (0, 0, 0), (10, -6, 4)],
)
def test_add(first_num, second_num, expected) -> None:
    calc = Calculator()
    assert expected == calc.add(first_num, second_num)


def test_sub() -> None:
    calc = Calculator()
    assert 3 == calc.subtract(5, 2)


def test_mul() -> None:
    calc = Calculator()
    assert 10 == calc.multiply(5, 2)


def test_div() -> None:
    calc = Calculator()
    assert 3.0 == calc.divide(6, 2)
