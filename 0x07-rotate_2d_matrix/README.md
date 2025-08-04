# 0x07. Rotate 2D Matrix

## 📝 Description

This project implements an algorithm to rotate an n×n 2D matrix 90 degrees clockwise in-place. This is a classic array manipulation problem that demonstrates matrix operations, space optimization, and geometric transformations.

The challenge focuses on understanding matrix indexing, in-place algorithms, and optimizing space complexity.

## 🎯 Learning Objectives

- Master 2D array manipulation and indexing
- Understand matrix rotation algorithms and geometric transformations
- Implement in-place algorithms for space optimization
- Practice pattern recognition in matrix operations

## 📋 Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow pycodestyle (version 2.8.0)
- All files must be executable
- All modules and functions must be documented
- Do not import any module

## 🚀 Implementation

### Function Prototype
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (List[List[int]]): The input 2D matrix to be rotated
        
    Returns:
        None: The matrix is modified in-place
    """
```

### Algorithm Strategy

The rotation is achieved through two main steps:
1. **Transpose the matrix**: Convert rows to columns
2. **Reverse each row**: Complete the 90-degree clockwise rotation

## 📁 Files

| File | Description |
|------|-------------|
| `0-rotate_2d_matrix.py` | Main implementation of 2D matrix rotation |
| `README.md` | Project documentation and usage guide |

## 🔍 Algorithm Explanation

### Visual Example

**Original Matrix:**
```
1 2 3
4 5 6  
7 8 9
```

**Step 1 - Transpose (swap matrix[i][j] with matrix[j][i]):**
```
1 4 7
2 5 8
3 6 9
```

**Step 2 - Reverse each row:**
```
7 4 1
8 5 2
9 6 3
```

### Detailed Steps:

1. **Transpose Operation**:
   ```python
   for i in range(n):
       for j in range(i + 1, n):
           matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   ```

2. **Row Reversal**:
   ```python
   for row in matrix:
       row.reverse()
   ```

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test 2D Matrix Rotation
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    rotate_2d_matrix(matrix)
    
    print("\nRotated Matrix (90° clockwise):")
    for row in matrix:
        print(row)
```

**Expected Output:**
```
Original Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Rotated Matrix (90° clockwise):
[7, 4, 1]
[8, 5, 2]
[9, 6, 3]
```

## 🔍 Algorithm Complexity

- **Time Complexity:** O(n²) - We visit each element exactly twice
- **Space Complexity:** O(1) - In-place rotation with constant extra space

## 💡 Key Concepts

### Matrix Operations:
- **Transpose**: Swapping elements across the main diagonal
- **Row Reversal**: Reversing elements within each row
- **In-place Modification**: Changing the original matrix without extra space

### Index Relationships:
For 90° clockwise rotation, element at `(i, j)` moves to `(j, n-1-i)`

### Geometric Understanding:
- 90° clockwise = Transpose + Reverse rows
- 90° counterclockwise = Reverse rows + Transpose
- 180° rotation = Reverse rows + Reverse columns

## 🧮 Mathematical Background

### Transformation Matrix for 90° Clockwise Rotation:
```
[0  1]   [x]   [y]
[-1 0] × [y] = [-x]
```

### Index Mapping:
- Original position: `(i, j)`
- New position: `(j, n-1-i)`
- Where `n` is the matrix dimension

## ✅ Testing

### Test with Different Sizes:

```python
#!/usr/bin/python3
"""
Comprehensive testing
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

def print_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print(row)

# Test 2x2 matrix
matrix_2x2 = [
    [1, 2],
    [3, 4]
]
print_matrix(matrix_2x2, "Original 2x2")
rotate_2d_matrix(matrix_2x2)
print_matrix(matrix_2x2, "Rotated 2x2")

# Test 4x4 matrix
matrix_4x4 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
print_matrix(matrix_4x4, "Original 4x4")
rotate_2d_matrix(matrix_4x4)
print_matrix(matrix_4x4, "Rotated 4x4")
```

### Edge Cases:
```python
# Test 1x1 matrix
matrix_1x1 = [[1]]
rotate_2d_matrix(matrix_1x1)
print(matrix_1x1)  # Should remain [[1]]

# Test empty matrix
matrix_empty = []
rotate_2d_matrix(matrix_empty)  # Should handle gracefully
```

## 🚨 Common Pitfalls

1. **Index Bounds**: Ensure `j` starts from `i+1` in transpose to avoid double-swapping
2. **Matrix Modification**: Remember that the operation is in-place
3. **Square Matrix Only**: Algorithm works only for n×n matrices
4. **Order of Operations**: Transpose first, then reverse rows

## 🔄 Alternative Approaches

### 1. Four-Way Swap (Single Pass):
```python
def rotate_four_way(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Store temp
            temp = matrix[i][j]
            # Move values in 4-way rotation
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
```

### 2. Layer-by-Layer Rotation:
Process matrix in concentric layers, rotating each layer independently.

## 🔗 Related Problems

- **Matrix Transpose**: Core operation used in rotation
- **Array Reversal**: Understanding row manipulation
- **Geometric Transformations**: Rotations, reflections, scaling
- **In-place Algorithms**: Space-efficient modifications

## 📚 Resources

- [Matrix Rotation Algorithms](https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/)
- [Geometric Transformations](https://en.wikipedia.org/wiki/Transformation_matrix)
- [In-place Matrix Operations](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Python List Operations](https://docs.python.org/3/tutorial/datastructures.html)
