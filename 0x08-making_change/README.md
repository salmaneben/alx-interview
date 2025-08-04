# 0x08. Making Change

## 📝 Description

This project solves the classic "Coin Change" problem using a greedy algorithm approach. Given a collection of coin denominations and a target amount, the algorithm determines the minimum number of coins needed to make that exact amount.

This challenge demonstrates optimization techniques, greedy algorithms, and edge case handling in algorithmic problem-solving.

## 🎯 Learning Objectives

- Understand and implement greedy algorithm strategies
- Learn to solve optimization problems with constraints
- Practice algorithmic thinking for financial/counting problems
- Master edge case handling and input validation

## 📋 Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable
- All modules and functions must be documented

## 🚀 Implementation

### Function Prototype
```python
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    
    Args:
        coins (List[int]): List of coin denominations available
        total (int): Target amount to make change for
        
    Returns:
        int: Fewest number of coins needed, or -1 if impossible
    """
```

### Problem Analysis

**Objective**: Find the minimum number of coins that sum to the target total.

**Approach**: Greedy algorithm - always use the largest coin denomination possible.

**Limitation**: This greedy approach works optimally only for certain coin systems (like standard currency systems).

## 📁 Files

| File | Description |
|------|-------------|
| `0-making_change.py` | Main implementation of coin change algorithm |
| `0-main.py` | Test file with example usage |
| `README.md` | Project documentation and usage guide |

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test Making Change implementation
"""
makeChange = __import__('0-making_change').makeChange

# Test cases
test_cases = [
    ([1, 2, 25], 37),           # Should return 7
    ([1256, 54, 48, 16, 102], 1453),  # Should return -1
    ([1, 5, 10, 25], 30),       # Should return 2
    ([2], 3),                   # Should return -1
    ([1], 0),                   # Should return 0
]

for coins, total in test_cases:
    result = makeChange(coins, total)
    print(f"Coins: {coins}, Total: {total} -> {result}")
```

**Expected Output:**
```
Coins: [1, 2, 25], Total: 37 -> 7
Coins: [1256, 54, 48, 16, 102], Total: 1453 -> -1
Coins: [1, 5, 10, 25], Total: 30 -> 2
Coins: [2], Total: 3 -> -1
Coins: [1], Total: 0 -> 0
```

## 🔍 Algorithm Explanation

### Step-by-Step Process:

1. **Input Validation**:
   ```python
   if total <= 0:
       return 0
   if not coins:
       return -1
   ```

2. **Sort Coins**: Sort in descending order for greedy approach
   ```python
   coins.sort(reverse=True)
   ```

3. **Greedy Selection**: Use largest coins first
   ```python
   for coin in coins:
       while remaining >= coin:
           count += remaining // coin
           remaining = remaining % coin
   ```

4. **Validation**: Check if exact amount was achieved
   ```python
   return count if remaining == 0 else -1
   ```

### Detailed Example:

**Making change for 37 with coins [1, 2, 25]:**

```
Step 1: Sort coins -> [25, 2, 1]
Step 2: Use 25s -> 37 ÷ 25 = 1 coin, remainder = 12
Step 3: Use 2s  -> 12 ÷ 2 = 6 coins, remainder = 0
Step 4: Total coins = 1 + 6 = 7
```

## 🔍 Algorithm Complexity

- **Time Complexity:** O(n log n + total) where n is number of coin types
  - O(n log n) for sorting
  - O(total) in worst case for coin counting
- **Space Complexity:** O(1) - Constant extra space

## 💡 Algorithm Limitations

### When Greedy Fails:
The greedy approach doesn't always produce optimal results for arbitrary coin systems.

**Example:**
- Coins: [1, 3, 4]
- Total: 6
- Greedy: 4 + 1 + 1 = 3 coins
- Optimal: 3 + 3 = 2 coins

### Coin Systems Where Greedy Works:
- **Standard Currency**: [1, 5, 10, 25, 50, 100] cents
- **Binary System**: Powers of 2
- **Any system where each coin ≥ 2× the previous coin**

## 🧮 Examples Breakdown

**Example 1: Standard coins**
```python
makeChange([1, 5, 10, 25], 67)
# Process: 25×2 + 10×1 + 5×1 + 1×2 = 6 coins
# Result: 6
```

**Example 2: Impossible case**
```python
makeChange([5, 10], 3)
# Cannot make 3 with only 5 and 10 denomination coins
# Result: -1
```

**Example 3: Edge case**
```python
makeChange([1, 2, 5], 0)
# No coins needed for amount 0
# Result: 0
```

## ✅ Testing

### Comprehensive Test Suite:

```python
#!/usr/bin/python3
"""
Comprehensive testing for makeChange
"""
makeChange = __import__('0-making_change').makeChange

def test_makeChange():
    # Test normal cases
    assert makeChange([1, 2, 25], 37) == 7
    assert makeChange([1, 5, 10, 25], 30) == 2
    
    # Test edge cases
    assert makeChange([1], 0) == 0
    assert makeChange([], 10) == -1
    assert makeChange([2], 3) == -1
    
    # Test large amounts
    assert makeChange([1, 5, 10, 25], 1000) == 40
    
    print("All tests passed!")

if __name__ == "__main__":
    test_makeChange()
```

## 🚨 Edge Cases to Consider

1. **Total ≤ 0**: Return 0 (no coins needed)
2. **Empty coin list**: Return -1 (impossible)
3. **No valid combination**: Return -1
4. **Large amounts**: Ensure algorithm efficiency
5. **Duplicate coins**: Handle properly in coin list
6. **Zero-value coins**: Filter out invalid denominations

## 🔄 Alternative Approaches

### 1. Dynamic Programming (Optimal Solution):
```python
def makeChangeDP(coins, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
```

### 2. BFS Approach:
Use breadth-first search to find minimum coins by exploring all possible combinations level by level.

## 🔗 Related Problems

- **Unbounded Knapsack**: Similar optimization structure
- **Minimum Path Sum**: Dynamic programming concepts
- **Partition Problem**: Subset selection challenges
- **Stock Span Problem**: Greedy algorithm applications

## 📚 Resources

- [Coin Change Problem - Dynamic Programming](https://www.geeksforgeeks.org/coin-change-dp-7/)
- [Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)
- [When Greedy Works for Coin Change](https://cs.stackexchange.com/questions/6552/when-can-a-greedy-algorithm-solve-the-coin-change-problem)
- [Algorithm Design Manual](http://www.algorist.com/) by Steven Skiena

## 🎯 Key Takeaways

1. **Greedy vs Optimal**: Understand when greedy algorithms work
2. **Edge Cases**: Always validate inputs and handle special cases
3. **Complexity Analysis**: Consider both time and space efficiency
4. **Real-world Application**: Coin change is used in POS systems and banking
5. **Algorithm Choice**: Sometimes simple approaches work well for specific constraints
