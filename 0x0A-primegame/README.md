# 0x0A. Prime Game

## 📝 Description

This project implements a competitive game theory problem involving prime numbers. Maria and Ben play a game where they alternately remove prime numbers and their multiples from a set of consecutive integers. The challenge combines game theory, prime number generation, and strategic analysis.

This problem demonstrates the Sieve of Eratosthenes algorithm, game theory concepts, and mathematical optimization.

## 🎯 Learning Objectives

- Understand game theory and optimal play strategies
- Implement the Sieve of Eratosthenes for efficient prime generation
- Analyze mathematical patterns in competitive scenarios
- Practice algorithm optimization for time-sensitive problems

## 📋 Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable
- All modules and functions must be documented
- Do not import any module

## 🚀 Implementation

### Function Prototype
```python
def isWinner(x, nums):
    """
    Determine the winner of Prime Game
    
    Args:
        x (int): Number of rounds
        nums (List[int]): Array of n for each round
    
    Returns:
        str: Name of winner ('Maria'/'Ben') or None if tie
    """
```

## 🎮 Game Rules

### Game Setup:
1. **Players**: Maria and Ben (Maria goes first)
2. **Starting Set**: Consecutive integers from 1 to n
3. **Turn Action**: Choose a prime number and remove it plus all its multiples
4. **Win Condition**: Player who cannot make a move loses
5. **Multiple Rounds**: Play x rounds with different n values

### Game Strategy:
- **Maria's Advantage**: Goes first in each round
- **Optimal Play**: Both players play optimally
- **Key Insight**: The winner depends on the count of available prime numbers

## 📁 Files

| File | Description |
|------|-------------|
| `0-prime_game.py` | Main implementation of prime game logic |
| `README.md` | Project documentation and usage guide |

## 🔍 Algorithm Explanation

### Core Game Theory Insight:
- If the number of prime numbers ≤ n is **odd**, Maria wins (she gets the last move)
- If the number of prime numbers ≤ n is **even**, Ben wins (he gets the last move)

### Implementation Steps:

1. **Prime Generation**: Use Sieve of Eratosthenes to find all primes up to n
2. **Game Analysis**: Count primes for each round
3. **Winner Determination**: Apply game theory rules
4. **Result Aggregation**: Count wins across all rounds

### Sieve of Eratosthenes Implementation:
```python
def get_primes_up_to(n):
    """Generate all prime numbers up to n efficiently"""
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i]]
```

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test Prime Game implementation
"""
isWinner = __import__('0-prime_game').isWinner

if __name__ == "__main__":
    # Test with multiple rounds
    x = 5
    nums = [2, 5, 1, 4, 3]
    
    winner = isWinner(x, nums)
    print(f"Winner: {winner}")
    
    # Individual round analysis
    for i, n in enumerate(nums):
        primes = get_primes_up_to(n)
        print(f"Round {i+1} (n={n}): {len(primes)} primes -> {'Maria' if len(primes) % 2 == 1 else 'Ben'}")
```

**Expected Output:**
```
Winner: Ben
Round 1 (n=2): 1 primes -> Maria
Round 2 (n=5): 3 primes -> Maria  
Round 3 (n=1): 0 primes -> Ben
Round 4 (n=4): 2 primes -> Ben
Round 5 (n=3): 2 primes -> Ben
```

## 🔍 Algorithm Complexity

- **Time Complexity:** O(n log log n) for sieve + O(x) for game analysis = O(max(nums) × log log max(nums) + x)
- **Space Complexity:** O(max(nums)) for the sieve array

## 💡 Game Theory Analysis

### Why the Strategy Works:

1. **Turn-Based Game**: Players alternate moves
2. **Perfect Information**: Both players see the complete game state
3. **Optimal Play**: Both players make the best possible moves
4. **Finite Game**: Game always ends (no infinite loops)

### Mathematical Proof:
- Each prime removal eliminates exactly one prime from future consideration
- Total number of moves = total number of primes ≤ n
- Maria makes moves 1, 3, 5, ... (odd-numbered moves)
- Ben makes moves 2, 4, 6, ... (even-numbered moves)
- Last move determines winner

## 🧮 Examples Breakdown

### Example 1: n = 4
```
Initial set: {1, 2, 3, 4}
Primes available: [2, 3]

Turn 1 (Maria): Choose 2, remove {2, 4} → Remaining: {1, 3}
Turn 2 (Ben): Choose 3, remove {3} → Remaining: {1}
Result: Ben wins (no more primes for Maria)

Prime count: 2 (even) → Ben wins ✓
```

### Example 2: n = 5
```
Initial set: {1, 2, 3, 4, 5}
Primes available: [2, 3, 5]

Turn 1 (Maria): Choose 2, remove {2, 4} → Remaining: {1, 3, 5}
Turn 2 (Ben): Choose 3, remove {3} → Remaining: {1, 5}
Turn 3 (Maria): Choose 5, remove {5} → Remaining: {1}
Result: Maria wins (no more primes for Ben)

Prime count: 3 (odd) → Maria wins ✓
```

## ✅ Testing

### Comprehensive Test Cases:

```python
#!/usr/bin/python3
"""
Test Prime Game with various scenarios
"""
isWinner = __import__('0-prime_game').isWinner

def test_game():
    # Test individual cases
    test_cases = [
        (1, [4], "Ben"),        # 2 primes (even) → Ben
        (1, [5], "Maria"),      # 3 primes (odd) → Maria
        (1, [1], "Ben"),        # 0 primes → Ben (no moves)
        (3, [4, 5, 1], "Ben"),  # Ben: 2, Maria: 1
        (5, [2, 5, 1, 4, 3], "Ben")  # Ben: 3, Maria: 2
    ]
    
    for x, nums, expected in test_cases:
        result = isWinner(x, nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} x={x}, nums={nums}: {result} (expected {expected})")

if __name__ == "__main__":
    test_game()
```

### Edge Cases:
```python
# Test edge cases
edge_cases = [
    (0, [], None),          # No rounds
    (1, [0], "Ben"),        # No primes available
    (2, [10, 1], "Ben"),    # Mixed large and small
    (1, [100], "Ben")       # Large number
]
```

## 🚨 Common Pitfalls

1. **Off-by-One Errors**: Correctly handle n=1 case (no primes)
2. **Tie Conditions**: Handle equal wins properly
3. **Large Numbers**: Ensure efficient prime generation
4. **Input Validation**: Handle invalid inputs gracefully

## 🎯 Optimization Techniques

### 1. Precompute Primes:
```python
# Compute all primes up to maximum possible n once
max_n = max(nums) if nums else 0
primes_count = precompute_prime_counts(max_n)
```

### 2. Memoization:
```python
# Cache prime counts for repeated n values
@lru_cache(maxsize=None)
def get_prime_count(n):
    return len(get_primes_up_to(n))
```

### 3. Early Termination:
```python
# Stop if clear winner emerges
if maria_wins > x // 2:
    return "Maria"
if ben_wins > x // 2:
    return "Ben"
```

## 🔗 Related Concepts

- **Sieve of Eratosthenes**: Efficient prime generation
- **Game Theory**: Minimax, optimal strategies
- **Dynamic Programming**: Memoization of subproblems
- **Number Theory**: Prime distribution, prime counting

## 📚 Resources

- [Game Theory Basics](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
- [Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
- [Prime Number Theorem](https://en.wikipedia.org/wiki/Prime_number_theorem)
- [Competitive Programming Techniques](https://cp-algorithms.com/)

## 🏆 Advanced Extensions

1. **Multiple Players**: Extend to n-player games
2. **Different Rules**: Allow removing composite numbers
3. **Scoring System**: Award points based on primes removed
4. **Real-time Play**: Implement with time constraints