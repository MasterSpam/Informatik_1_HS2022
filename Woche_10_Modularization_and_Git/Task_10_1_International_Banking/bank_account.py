#!/usr/bin/env python3

from currency_converter import convert
from exchange_rates import EXCHANGE_RATES as rates


class BankAccount:

    def __init__(self, currency="CHF"):
        if currency not in rates:
            raise Warning("Bank accounts must have a valid currency")
        self._currency = currency
        self._balance = 0

    def get_currency(self):
        my_currency = self._currency
        return my_currency

    def get_balance(self):
        my_balance = self._balance
        return my_balance

    def deposit(self, amount, currency="CHF"):
        self._balance += amount if currency == self._currency else convert(amount, currency, self._currency)

    def withdraw(self, amount, currency="CHF"):
        self._balance -= amount if currency == self._currency else convert(amount, currency, self._currency)
        if self._balance < 0:
            raise Warning("Bank accounts must be positive")
