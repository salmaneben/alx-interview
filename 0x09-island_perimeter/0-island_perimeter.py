#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
        grid (List[List[int]]): A 2D grid where:
            - 0 represents water
            - 1 represents land
            
    Returns:
        int: The perimeter of the island
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 adjacent cells
                # Top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter