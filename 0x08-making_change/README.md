# Making Change

## Description
This project contains a solution for calculating the minimum number of coins needed to reach a target amount. It uses a greedy algorithm approach to solve the coin change problem efficiently.

## Problem Statement
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

## Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
- `coins`: List of integers representing the values of coins available
- `total`: Target total to make change for

### Returns
- Returns fewest number of coins needed to meet total
- Returns 0 if total is 0 or less
- Returns -1 if total cannot be met by any combination of coins

## Examples
```python
makeChange([1, 2, 25], 37)
# Output: 7 (25 + 2 + 2 + 2 + 2 + 2 + 2 = 37)

makeChange([1256, 54, 48, 16, 102], 1453)
# Output: -1 (impossible to make this amount)
```

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)

## File Structure
- `0-making_change.py`: Contains the solution function
- `0-main.py`: Main test file

## Algorithm
The solution uses a greedy approach by:
1. Sorting coins in descending order
2. Iteratively using the largest possible coin
3. Keeping track of the remaining amount
4. Counting the minimum coins needed

## Time Complexity
- Time Complexity: O(n), where n is the number of coin denominations
- Space Complexity: O(1)
