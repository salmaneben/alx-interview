# 0x00. Pascal's Triangle

## 📝 Description

This project implements a function to generate Pascal's Triangle, a triangular array of numbers where each number is the sum of the two numbers directly above it. This is a classic algorithmic problem that demonstrates dynamic programming concepts and mathematical pattern recognition.

## 🎯 Learning Objectives

- Understand and implement Pascal's Triangle algorithm
- Work with nested lists and dynamic programming
- Practice mathematical problem-solving in code
- Master list manipulation and indexing in Python

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
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n
    
    Args:
        n (int): The number of rows in Pascal's triangle
        
    Returns:
        List[List[int]]: Pascal's triangle as nested lists
        Returns empty list if n <= 0
    """
```

### Algorithm Explanation

Pascal's Triangle follows these rules:
1. The first and last elements of each row are always 1
2. Each interior element is the sum of the two elements above it
3. Row `i` has `i+1` elements

**Example:**
```
Row 0:      1
Row 1:     1 1
Row 2:    1 2 1
Row 3:   1 3 3 1
Row 4:  1 4 6 4 1
```

## 📁 Files

| File | Description |
|------|-------------|
| `0-pascal_triangle.py` | Main implementation of Pascal's Triangle algorithm |
| `README.md` | Project documentation and usage guide |

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test Pascal's Triangle implementation
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """Print Pascal's triangle in a formatted way"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

**Expected Output:**
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## 🔍 Algorithm Complexity

- **Time Complexity:** O(n²) - We need to generate n rows with increasing elements
- **Space Complexity:** O(n²) - Storage for the entire triangle

## 💡 Key Concepts

- **Dynamic Programming**: Building each row based on the previous row
- **Mathematical Patterns**: Understanding Pascal's Triangle properties
- **List Manipulation**: Creating and modifying nested Python lists
- **Edge Case Handling**: Managing n <= 0 cases

## 🧮 Mathematical Background

Pascal's Triangle has many interesting mathematical properties:
- Each row represents binomial coefficients
- Sum of each row equals 2^n where n is the row number
- The triangle is symmetric
- Contains Fibonacci numbers along diagonals

## ✅ Testing

Run the implementation with various test cases:

```bash
# Test with different values
python3 -c "
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
print('n=0:', pascal_triangle(0))
print('n=1:', pascal_triangle(1))
print('n=5:', pascal_triangle(5))
"
```

## 🔗 Related Problems

- Binomial Coefficients
- Dynamic Programming fundamentals
- Array manipulation challenges
- Mathematical sequence generation

## 📚 Resources

- [Pascal's Triangle - Wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [Dynamic Programming Concepts](https://www.geeksforgeeks.org/dynamic-programming/)
- [Python List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
