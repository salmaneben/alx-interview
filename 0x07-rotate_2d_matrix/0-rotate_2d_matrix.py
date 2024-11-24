#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise.
    Args:
        matrix (List[List[int]]): The input 2D matrix to be rotated.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Then, reverse each row
    for row in matrix:
        row.reverse()
