# 0x02. Minimum Operations

## 📝 Description

This project solves the "Minimum Operations" problem: Given a text editor that can only perform two operations (Copy All and Paste), determine the minimum number of operations needed to achieve exactly `n` 'H' characters starting from a single 'H'.

This problem demonstrates the application of mathematical optimization, prime factorization, and greedy algorithms.

## 🎯 Learning Objectives

- Understand prime factorization and its applications
- Apply greedy algorithm strategies
- Solve optimization problems with mathematical insights
- Practice algorithmic thinking for complex problems

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
def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The desired number of H characters

    Returns:
        int: The minimum number of operations needed, or 0 if impossible
    """
```

### Problem Analysis

**Available Operations:**
1. **Copy All**: Copy all characters currently in the file
2. **Paste**: Paste the copied characters

**Strategy:**
The key insight is that to reach `n` characters optimally, we need to find the prime factorization of `n`. Each prime factor represents a "copy-and-paste cycle."

**Example for n = 12:**
- 12 = 2 × 2 × 3
- Operations: 2 + 2 + 3 = 7 total operations

## 📁 Files

| File | Description |
|------|-------------|
| `0-minoperations.py` | Main implementation of minimum operations algorithm |
| `README.md` | Project documentation and usage guide |

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test Minimum Operations implementation
"""
minOperations = __import__('0-minoperations').minOperations

if __name__ == "__main__":
    test_cases = [0, 1, 4, 9, 12, 21]
    
    for n in test_cases:
        result = minOperations(n)
        print(f"n = {n}: {result} operations")
```

**Expected Output:**
```
n = 0: 0 operations
n = 1: 0 operations  
n = 4: 4 operations  (2 + 2)
n = 9: 6 operations  (3 + 3)
n = 12: 7 operations (2 + 2 + 3)
n = 21: 8 operations (3 + 7)
```

## 🔍 Algorithm Explanation

### Step-by-Step Process:

1. **Edge Cases**: If n ≤ 1, return 0 (impossible or already achieved)

2. **Prime Factorization**: Find all prime factors of n
   ```
   n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ
   ```

3. **Sum of Factors**: The minimum operations equal the sum of all prime factors (with repetition)
   ```
   operations = (p₁ × a₁) + (p₂ × a₂) + ... + (pₖ × aₖ)
   ```

### Why This Works:

- To create `p` copies from 1 character: Copy All (1) + Paste (p-1) = p operations
- For composite numbers, it's always more efficient to build through factors
- Prime factorization gives the optimal decomposition

## 🔍 Algorithm Complexity

- **Time Complexity:** O(√n) - We only check divisors up to √n
- **Space Complexity:** O(1) - Constant extra space

## 💡 Mathematical Insight

**Key Theorem**: The minimum number of operations to reach `n` characters equals the sum of prime factors of `n` (counting multiplicities).

**Proof Intuition**:
- Each prime factor `p` requires exactly `p` operations to multiply the current count by `p`
- Composite factors are always suboptimal compared to their prime factorization

## 🧮 Examples Breakdown

**Example 1: n = 9**
```
9 = 3 × 3
Operations needed: 3 + 3 = 6

Step by step:
H         (start)
HHH       (Copy All, Paste, Paste) - 3 operations  
HHHHHHHHH (Copy All, Paste, Paste) - 3 more operations
Total: 6 operations
```

**Example 2: n = 12**
```
12 = 2 × 2 × 3
Operations needed: 2 + 2 + 3 = 7

Building path: 1 → 2 → 4 → 12
```

## ✅ Testing

Test with various cases:

```bash
# Test edge cases and various numbers
python3 -c "
minOperations = __import__('0-minoperations').minOperations
test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 21]
for n in test_cases:
    print(f'{n}: {minOperations(n)} operations')
"
```

## 🔗 Related Concepts

- **Prime Factorization**: Core mathematical concept
- **Greedy Algorithms**: Choosing optimal local choices
- **Dynamic Programming**: Alternative approach for similar problems
- **Number Theory**: Understanding divisibility and factors

## 📚 Resources

- [Prime Factorization Algorithms](https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/)
- [Greedy Algorithm Strategies](https://www.geeksforgeeks.org/greedy-algorithms/)
- [Mathematical Optimization](https://en.wikipedia.org/wiki/Mathematical_optimization)