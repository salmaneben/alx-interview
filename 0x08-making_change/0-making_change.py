#!/usr/bin/python3
"""
Module for determining the minimum number of coins needed to meet a total
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total
    
    Args:
        coins (list): List of coin values
        total (int): Target total to make change for
        
    Returns:
        int: Fewest number of coins needed to meet total
             Returns 0 if total is 0 or less
             Returns -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    dp = [0] + [total + 1] * total

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1