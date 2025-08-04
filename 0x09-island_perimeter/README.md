# 0x09. Island Perimeter

## 📝 Description

This project calculates the perimeter of an island represented in a 2D grid. The island is formed by connected land cells (1s) surrounded by water cells (0s). This problem demonstrates grid traversal, boundary detection, and 2D array manipulation techniques.

The challenge focuses on understanding grid navigation, neighbor checking, and efficient boundary calculation.

## 🎯 Learning Objectives

- Master 2D grid traversal and manipulation
- Understand boundary detection algorithms
- Practice neighbor-checking techniques in grids
- Learn efficient iteration over 2D arrays

## 📋 Requirements

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should follow PEP 8 style (version 1.7.x)
- All files must be executable
- All modules and functions must be documented
- Do not import any module

## 🚀 Implementation

### Function Prototype
```python
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
```

### Problem Constraints
- Grid cells are either 0 (water) or 1 (land)
- Grid cells are connected horizontally/vertically (not diagonally)
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water around the island)

## 📁 Files

| File | Description |
|------|-------------|
| `0-island_perimeter.py` | Main implementation of island perimeter calculation |
| `0-main.py` | Test file with sample grid |
| `README.md` | Project documentation and usage guide |

## 🔍 Algorithm Explanation

### Core Strategy:
For each land cell (1), count how many of its 4 sides are exposed to water or the grid boundary.

### Step-by-Step Process:

1. **Iterate through each cell** in the grid
2. **For each land cell (1)**:
   - Check all 4 adjacent directions (up, down, left, right)
   - Add 1 to perimeter for each side that:
     - Is at the grid boundary, OR
     - Is adjacent to a water cell (0)

### Direction Checking:
```python
# For cell at position (i, j), check:
# Top:    (i-1, j)
# Bottom: (i+1, j) 
# Left:   (i, j-1)
# Right:  (i, j+1)
```

## 🧪 Usage Example

```python
#!/usr/bin/python3
"""
Test Island Perimeter implementation
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    
    print(f"Island perimeter: {island_perimeter(grid)}")
```

**Expected Output:**
```
Island perimeter: 12
```

### Visual Breakdown:

```
0 0 0 0 0 0
0 1 0 0 0 0  ← Land cell: 4 exposed sides
0 1 0 0 0 0  ← Land cell: 3 exposed sides (connected to cell above)
0 1 1 1 0 0  ← Land cells: various exposed sides
0 0 0 0 0 0

Total perimeter: 12
```

## 🔍 Algorithm Complexity

- **Time Complexity:** O(m × n) where m and n are grid dimensions
- **Space Complexity:** O(1) - Constant extra space

## 💡 Detailed Algorithm Logic

### Boundary Conditions:
```python
# Top edge exposed if:
if i == 0 or grid[i-1][j] == 0:
    perimeter += 1

# Bottom edge exposed if:
if i == rows-1 or grid[i+1][j] == 0:
    perimeter += 1

# Left edge exposed if:
if j == 0 or grid[i][j-1] == 0:
    perimeter += 1

# Right edge exposed if:
if j == cols-1 or grid[i][j+1] == 0:
    perimeter += 1
```

### Edge Cases Handled:
1. **Grid boundaries**: Edges at grid limits are always exposed
2. **Water neighbors**: Adjacent water cells create exposed edges
3. **Empty grid**: Returns 0
4. **Single cell island**: Returns 4 (all sides exposed)

## 🧮 Examples Breakdown

### Example 1: Simple Rectangle
```python
grid = [
    [1, 1],
    [1, 1]
]
# Each corner cell has 2 exposed sides
# Each edge cell has 1 exposed side
# Perimeter = 8
```

### Example 2: Single Cell
```python
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
# Single land cell has all 4 sides exposed
# Perimeter = 4
```

### Example 3: L-Shape
```python
grid = [
    [1, 1, 0],
    [1, 0, 0],
    [1, 0, 0]
]
# Calculate each cell's contribution:
# (0,0): top + left = 2
# (0,1): top + right = 2  
# (1,0): left + right = 2
# (2,0): left + bottom + right = 3
# Total = 10
```

## ✅ Testing

### Comprehensive Test Cases:

```python
#!/usr/bin/python3
"""
Test various island configurations
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

def test_cases():
    # Test empty grid
    assert island_perimeter([]) == 0
    
    # Test single cell
    assert island_perimeter([[1]]) == 4
    
    # Test no island
    assert island_perimeter([[0, 0], [0, 0]]) == 0
    
    # Test rectangle
    grid_rect = [
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert island_perimeter(grid_rect) == 10
    
    # Test complex shape
    grid_complex = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    result = island_perimeter(grid_complex)
    print(f"Complex island perimeter: {result}")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
```

## 🎯 Alternative Approaches

### Method 1: Count Land Cells and Connections
```python
def island_perimeter_alt(grid):
    if not grid:
        return 0
    
    land_cells = 0
    connections = 0
    
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                land_cells += 1
                # Count connections to right
                if j + 1 < cols and grid[i][j+1] == 1:
                    connections += 1
                # Count connections below
                if i + 1 < rows and grid[i+1][j] == 1:
                    connections += 1
    
    return land_cells * 4 - connections * 2
```

### Method 2: DFS/BFS Traversal
Use depth-first search to traverse the island and count boundary edges during traversal.

## 🌊 Real-World Applications

- **Geographic Information Systems (GIS)**: Calculating coastline lengths
- **Image Processing**: Object boundary detection
- **Game Development**: Collision detection and map boundaries
- **Urban Planning**: Property boundary calculations

## 🚨 Common Pitfalls

1. **Index Out of Bounds**: Always check grid boundaries
2. **Wrong Neighbor Check**: Ensure proper direction checking
3. **Double Counting**: Each edge should be counted exactly once
4. **Edge Case Handling**: Empty grids, single cells, no islands

## 🔗 Related Problems

- **Number of Islands**: Count separate island groups
- **Max Area of Island**: Find largest connected land area
- **Surrounded Regions**: Flood fill algorithms
- **Word Search**: Grid traversal with backtracking

## 📚 Resources

- [2D Array Manipulation](https://www.geeksforgeeks.org/multidimensional-arrays-in-python/)
- [Grid Traversal Patterns](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-stack/)
- [Flood Fill Algorithm](https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/)
- [Connected Components](https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/)

## 🎮 Practice Extensions

1. **Multiple Islands**: Modify to handle multiple separate islands
2. **Island Areas**: Calculate area along with perimeter
3. **Irregular Grids**: Handle non-rectangular grid shapes
4. **3D Extension**: Calculate surface area of 3D objects