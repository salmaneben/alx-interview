#!/usr/bin/python3
"""
Making Change Solution
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount
    """
    if total <= 0:
        return 0

    if not coins:
        return -1

    # Initialize array to store minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # For each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                # Update if we can get a better result using this coin
                if dp[amount - coin] != float('inf'):
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
