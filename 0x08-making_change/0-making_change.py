#!/usr/bin/python3
"""
Making Change Solution
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount
    Args:
        coins: list of coins of different values
        total: total amount to meet
    Returns:
        fewest number of coins needed to meet total
        or -1 if total cannot be met by any combination of coins
    """
    if total <= 0:
        return 0

    # Initialize array to store minimum coins needed for each amount
    dp = [0] + [float('inf')] * total

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
