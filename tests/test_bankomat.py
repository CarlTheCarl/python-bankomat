import pytest
from bankomat import Bankomat
from account import Account
from card import Card

def test_insert_card():
    bankomat = Bankomat()
    account = Account("Benjamin", "Berglund", "700109-2456")
    card = Card(account)
    result = bankomat.insert_card(card)
    assert isinstance(result, Card)

def test_eject_card():
    bankomat = Bankomat()
    account = Account("Benjamin", "Berglund", "700109-2456")
    card = Card(account)
    bankomat.insert_card(card)
    bankomat.eject_card()
    assert not isinstance(bankomat.card, Card)

def test_enter_invalid_pin():
    bankomat = Bankomat()
    account = Account("Benjamin", "Berglund", "700109-2456")
    card = Card(account)
    bankomat.insert_card(card)
    result = bankomat.enter_pin("1234")
    assert result == False

def test_enter_valid_pin():
    bankomat = Bankomat()
    account = Account("Benjamin", "Berglund", "700109-2456")
    card = Card(account)
    bankomat.insert_card(card)
    result = bankomat.enter_pin("0123")
    assert result == True

    def test_three_strikes():
        bankomat = Bankomat()
        account = Account("Benjamin", "Berglund", "700109-2456")
        card = Card(account)
        bankomat.insert_card(card)
        bankomat.enter_pin("3214")
        bankomat.enter_pin("9999")
        result = bankomat.enter_pin("TreFemNioTvå")
        assert result is None


def test_money_withdrawal():
    initial_bankomat_balance = 110000
    initial_account_balance = 1000
    withdrawal = 1000
    bankomat = Bankomat()
    bankomat.machine_balance = initial_bankomat_balance
    account = Account("Benjamin", "Berglund", "700109-2456", initial_account_balance)
    card = Card(account)
    bankomat.insert_card(card)
    bankomat.enter_pin("0123")
    result = bankomat.withdraw(withdrawal)
    assert result == withdrawal
    assert account.balance == initial_account_balance - withdrawal
    assert bankomat.machine_balance + result == initial_bankomat_balance