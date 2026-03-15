from ex5_classes.bank_account import BankAccount
import pytest

account = BankAccount("ACC123456")

def test_normal():
    account.deposit(1000.0)
    assert account.balance == 1000.0
    account.withdraw(300.0)
    assert account.balance == 700.0

def test_encapsulation():
    with pytest.raises(AttributeError):
        account.balance = 5000.0

def test_deposit_zero():
    with pytest.raises(ValueError):
        account.deposit(0)

def test_deposit_negative():
    with pytest.raises(ValueError):
        account.deposit(-1000)

def test_withdraw_zero():
    with pytest.raises(ValueError):
        account.withdraw(0)
