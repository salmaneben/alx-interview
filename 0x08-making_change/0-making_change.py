#!/usr/bin/python3
"""
Module for making change problem using dynamic programming
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
    # Handle base cases
    if total <= 0:
        return 0
        
    # Sort coins in descending order for optimization
    coins.sort(reverse=True)
    
    # Initialize dp array with total + 1 (impossible value)
    # dp[i] represents minimum coins needed for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Build solution for all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Update minimum coins needed if using this coin leads to better solution
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return -1 if no solution found, otherwise return minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1