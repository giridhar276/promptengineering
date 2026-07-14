from decimal import Decimal

class InsufficientFundsError(Exception):
    pass

def transfer(balance_from: Decimal, balance_to: Decimal, amount: Decimal):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if balance_from < amount:
        raise InsufficientFundsError("insufficient funds")
    return balance_from - amount, balance_to + amount
