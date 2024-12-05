def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    
    Args:
    grid (List[List[int]]): A 2D grid where 0 represents water and 1 represents land.
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            # Check if current cell is land
            if grid[r][c] == 1:
                # Start with 4 sides
                cell_perimeter = 4
                
                # Check adjacent cells and subtract sides that touch land
                # Check cell above
                if r > 0 and grid[r-1][c] == 1:
                    cell_perimeter -= 1
                
                # Check cell below
                if r < rows - 1 and grid[r+1][c] == 1:
                    cell_perimeter -= 1
                
                # Check cell to the left
                if c > 0 and grid[r][c-1] == 1:
                    cell_perimeter -= 1
                
                # Check cell to the right
                if c < cols - 1 and grid[r][c+1] == 1:
                    cell_perimeter -= 1
                
                # Add this cell's perimeter to total
                perimeter += cell_perimeter
    
    return perimeter
