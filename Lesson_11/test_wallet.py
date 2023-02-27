import pytest
from wallet import Wallet

def test_default_init_amount():
    wallet = Wallet(0)
    assert wallet.balance == 0

def test_setup_init_amount():
    wallet = Wallet(1000000)
    assert wallet.balance == 1000000

def test_wallet_spend_cash():
    wallet = Wallet(100)
    wallet.spend_cash(15)
    assert wallet.balance == 85

def test_wallet_spend_cash_exception():
    wallet = Wallet(100)
    with pytest.raises(Exception):
        wallet.spend_cash(120)

def test_wallet_add_cash():
    wallet = Wallet(200)
    wallet.add_cash(34)
    assert wallet.balance == 234

