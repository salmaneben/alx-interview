#!/usr/bin/python3
'''
island perimeter
'''

def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the four sides and add to the perimeter if they are water or out of bounds
                if i == 0 or grid[i-1][j] == 0:  # Check top side
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Check bottom side
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Check left side
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Check right side
                    perimeter += 1
                    
    return perimeter