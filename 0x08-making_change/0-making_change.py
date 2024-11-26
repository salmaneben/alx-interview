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

    # Initialize an array to store the minimum coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # For each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                if min_coins[amount - coin] != float('inf'):
                    min_coins[amount] = min(min_coins[amount],
                                         min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1