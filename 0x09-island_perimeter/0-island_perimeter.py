#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    Args:
        grid (list): list of list of integers representing an island
    Returns:
        The perimeter of the island defined in grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Count adjacent water cells and edges
                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right
                if j == len(grid[0])-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
    return perimeter