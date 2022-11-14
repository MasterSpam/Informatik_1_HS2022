#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def max_profit(prices):
    profit = 0

    if type(prices) != list:
        return "Invalid Input Type"

    if not prices:
        return "Empty Price List"

    if len(prices) == 1:
        return 0

    for i in range(len(prices)):

        if type(prices[i]) != int:
            return "Invalid Data Type within List"

        if prices[i] < 0:
            return "Invalid Prices"

        if max(prices[:i + 1]) - min(prices[:i + 1]) > profit:
            profit = max(prices[:i + 1]) - min(prices[:i + 1])

    if prices == sorted(prices, reverse=True):
        return 0

    return profit


print(max_profit([4, 1, 2, 3, 1, 7, 5, 9, 3]))
