# Approved by: Arin

import pytest # Use 'python3 -m pytest' command to run tests
from bank_account import BankAccount

@pytest.fixture
def setup_account():
    return BankAccount(123456789)

def test_init_balance(setup_account):
    assert setup_account.balance == 0, "New account's balance should be initialized to 0."
    assert setup_account.id == 123456789, "ID num should be equal to ID created on setup."

def test_deposit(setup_account):
    setup_account.deposit(1000)
    assert setup_account.balance == 1000, "Balance should be 1000 after deposit."

def test_withdraw_success(setup_account):
    setup_account.deposit(1000)
    assert setup_account.withdraw(300), "Deposit 1000 and Withdraw 300 should return true."
    assert setup_account.balance == 700, "Balance after withdrawal should be 700."

def test_withdraw_fail(setup_account):
    setup_account.deposit(1000)
    assert not setup_account.withdraw(2000), "Withdraw 2000 from 1000 should return false."
    assert setup_account.balance == 1000, "Balance should remain 1000 after failed withdrawal."

def test_teardown(setup_account):
    setup_account = None
    assert setup_account is None, "Account should not be exist after closing."