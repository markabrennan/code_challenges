"""
New attempt at Rotting Oranges (Leet Code) 
using queue
"""

from collections import deque

def get_adj(grid, i, j):
    a = []
    if i+1 < len(grid) and grid[i+1][j] == 1:
        a.append((i+1, j))
    if j+1 < len(grid[i]) and grid[i][j+1] == 1:
        a.append((i, j+1))
    if i-1 >= 0 and grid[i-1][j] == 1:
        a.append((i-1, j))
    if j-1 >= 0 and grid[i][j-1] == 1:
        a.append((i, j-1))
    return a

def find_first(grid):
    ret = None 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                if (i+1 < len(grid) and grid[i+1][j] == 1) or (j+1 < len(grid[i]) and grid[i][j+1] == 1) or (i-1 >= 0 and grid[i-1][j] == 1) or (j-1 >= 0 and grid[i][j-1] == 1):
                    return (i, j)
    return ret

def r(grid):
    depth = 0            
    adj_q = deque()

    # find rotten organge
    first_orange = find_first(grid)
    adjacent = get_adj(grid, first_orange[0], first_orange[1])

    print(adjacent)
    if adjacent:
        for a in adjacent:
            adj_q.append((a[0], a[1], depth+1))
    
    print(adj_q)

    while adj_q:
        x, y, depth = adj_q.popleft()
        print(f'just popped - x: {x}, y: {y}, d: {depth}')
        # rot:
        grid[x][y] = 2
        nxt = get_adj(grid, x, y)
        print(f'next organge: {nxt} | depth: {depth+1}')
        for a in nxt:
            adj_q.append((a[0], a[1], depth+1))

    print(f'depth is now: {depth}')
    print(grid)

    for row in grid:
        if 1 in row:
            return -1    

    return depth


#m =  [[2,1,1],[1,1,0],[0,1,1]]  # --> 4
#m =  [[2,1,1],[0,1,0],[1,0,1]]  # --> -1
#m = [[0,2]]
#m = [[1,2]]
#m = [[1]]
#m = [[2,2,2,1,1]]
#m = [[0,2]]                 
#m = [[1,1,2,0,2,0]]  # --> 2
#m = [[1],[1],[1],[1]]  # --> -1
#m = [[1,2,1,1,2,1,1]]  # --> 2
#m = [[2,1,1],[0,1,1],[1,0,1]]  # --> -1
#m = [[0]]  # --> 0
#m = [[2],[2],[1],[0],[1],[1]] # --> -1
#m = [[0,1],[2,0]]  # --> -1
#m = [[0,0,1,1,1,1,1,2,1]]  # --> 5
#m = [[1],[2],[2]]  # --> 1
#m = [[2,2,2,1,1]] # --> 2
m = [[1,2,1,1,2,1,1]]  # --> 2




print(r(m))