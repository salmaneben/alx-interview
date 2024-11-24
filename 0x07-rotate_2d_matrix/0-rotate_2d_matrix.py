#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a n x n 2D matrix 90 degrees clockwise in-place
    Args:
        matrix: a n x n 2D matrix
    """
    n = len(matrix)
    # Transpose matrix
    for row in range(n):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # Reverse rows
    for row in range(n):
        matrix[row].reverse()