#!/usr/bin/python3
"""Module for calculating island perimeter."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island.

    Args:
        grid (list): 2D list of integers representing an island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter