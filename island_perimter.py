"""
Leet Code Problem 463: Island Perimeter
"""

def islandPerimeter(grid):
    perim = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perim += calc_perim(grid, i, j)

    return perim
    
def calc_perim(grid, i, j):
    perim = 0
    if (i+1 < len(grid) and grid[i+1][j] == 0) or i+1 >= len(grid):
        perim += 1
    if (j+1 < len(grid[i]) and grid[i][j+1] == 0) or j+1 >= len(grid[i]):
        perim += 1
    if (i-1 >= 0 and grid[i-1][j] == 0) or i-1 < 0:
        perim += 1
    if (j-1 >= 0 and grid[i][j-1] == 0) or j-1 < 0:
        perim += 1

    print(f'perim for this cell: {i}, {j}: {perim}')
    return perim

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

print(islandPerimeter(grid))

