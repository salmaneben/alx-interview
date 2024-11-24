#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a n x n 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix: n x n 2D matrix
    Returns:
        None
    """
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            # Swap elements across diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()