#!/usr/bin/python3
"""
Module to calculate island perimeter
"""


def island_perimeter(grid):
    """
    Calculate island perimeter from grid
    Args:
        grid (list): List of list of integers
        0 represents water
        1 represents land
    Return:
        Perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                continue
                
            if i == 0 or grid[i-1][j] == 0:    # top
                perimeter += 1
            if i == rows-1 or grid[i+1][j] == 0:  # bottom
                perimeter += 1
            if j == 0 or grid[i][j-1] == 0:    # left
                perimeter += 1
            if j == cols-1 or grid[i][j+1] == 0:  # right
                perimeter += 1

    return perimeter