#!/usr/bin/python3
"""
Function to calculate island perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island where:
    0 represents a water zone
    1 represents a land zone
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 sides
                # Left side
                if j == 0:
                    perimeter += 1
                elif grid[i][j-1] == 0:
                    perimeter += 1
                
                # Right side
                if j == cols-1:
                    perimeter += 1
                elif grid[i][j+1] == 0:
                    perimeter += 1
                
                # Top side
                if i == 0:
                    perimeter += 1
                elif grid[i-1][j] == 0:
                    perimeter += 1
                
                # Bottom side
                if i == rows-1:
                    perimeter += 1
                elif grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter