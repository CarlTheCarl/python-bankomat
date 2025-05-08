import pytest
from account import Account

def test_account_creation():
    account = Account("Benjamin", "Berglund", "700109-2456")
    assert len(account.ssn) == 11 or len(account.ssn) == 13

def test_zero_cash():
    account = Account("Benjamin", "Berglund", "700109-2456")
    assert account.balance == 0

def test_some_cash():
    account = Account("Benjamin", "Berglund", "700109-2456", 5)
    assert account.balance == 5