# Rotate 2D Matrix

## Description
This project contains a function that rotates an n x n 2D matrix 90 degrees clockwise in-place.

## Task 0: Rotate 2D Matrix
The function `rotate_2d_matrix(matrix)` takes an n x n 2D matrix as input and rotates it 90 degrees clockwise. The rotation is performed in-place, meaning the original matrix is modified directly without using additional matrices.

### Requirements
- The function takes a matrix parameter
- The matrix must be edited in-place
- The matrix will have 2 dimensions and will not be empty

### Example
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Environment
- Ubuntu 20.04 LTS
- Python 3.8.10
- Pycodestyle 2.8.0