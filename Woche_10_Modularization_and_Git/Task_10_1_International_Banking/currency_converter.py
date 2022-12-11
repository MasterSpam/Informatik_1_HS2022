#!/usr/bin/env python3

from exchange_rates import EXCHANGE_RATES as rates


def convert(amount, from_currency, to_currency):
    if type(amount) != int and type(amount) != float:
        raise Warning("Invalid amount Input")

    if amount <= 0:
        raise Warning("no negative amount allowed")

    if not from_currency or not to_currency or type(from_currency) != str or type(to_currency) != str:
        raise Warning("Invalid currency Input")

    if from_currency not in rates or to_currency not in rates:
        raise Warning("No Currency Exchange found")

    if to_currency in rates[from_currency]:
        amount = amount * rates[from_currency][to_currency]
        return amount

    if from_currency in rates[to_currency]:
        amount = amount / rates[to_currency][from_currency]
        return amount

    raise Warning("No Currency Exchange found")
