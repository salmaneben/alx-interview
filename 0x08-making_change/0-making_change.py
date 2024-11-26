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

    temp = [float('inf')] * (total + 1)
    temp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if temp[i - coin] != float('inf'):
                temp[i] = min(temp[i], temp[i - coin] + 1)

    if temp[total] == float('inf'):
        return -1

    return temp[total]