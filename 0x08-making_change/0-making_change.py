#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    remaining = total

    for coin in coins:
        while remaining >= coin:
            count += remaining // coin
            remaining = remaining % coin

        if remaining == 0:
            return count

    return -1