import pytest
from basic_pytest_learning.banking_system import OmBank


@pytest.fixture
def zero_bal_account():
    return OmBank()


@pytest.fixture
def initial_bal_account():
    return OmBank(50.0)


def test_open_bank_account_with_zero_balance(zero_bal_account) -> None:
    # ob = OmBank()
    # assert 0 == ob.balance
    assert 0 == zero_bal_account.balance


def test_open_bank_account_with_some_initial_deposit(initial_bal_account) -> None:
    # ob = OmBank(50)
    # assert 50 == ob.balance
    assert 50 == initial_bal_account.balance


def test_add_deposit_to_zero_bal_account(zero_bal_account) -> None:
    zero_bal_account.deposit(10)
    assert 10 == zero_bal_account.balance


def test_add_deposit_initial_bal_account(initial_bal_account) -> None:
    initial_bal_account.deposit(50)
    assert 100 == initial_bal_account.balance


def test_withdraw_from_a_zero_balance_acoount(zero_bal_account) -> None:
    assert 0 == zero_bal_account.balance


def test_withdraw_from_a_initial_balance_acoount(initial_bal_account) -> None:
    initial_bal_account.withdraw(20)
    assert 30 == initial_bal_account.balance


def test_try_to_with_draw_more_that_the_account_has(initial_bal_account) -> None:
    initial_bal_account.deposit(20)
    initial_bal_account.withdraw(100)
    assert 70 == initial_bal_account.balance


def test_collect_interest() -> None:
    ob = OmBank(50)
    assert 55 == round(ob.collect_interest())
