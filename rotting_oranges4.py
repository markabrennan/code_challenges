"""
Another, fresh, attempt at Rotting Oranges.
Key is to ensure I get the queue operations down
corrrectly.
"""

from collections import deque

def oranges_rotting(grid):
    def get_adj(i, j):
        adj = []
        if i+1 < len(grid) and grid[i+1][j] == 1:
            adj.append((i+1, j))
        if j+1 < len(grid[i]) and grid[i][j+1] == 1:
            adj.append((i,j+1))
        if i-1 >= 0 and grid[i-1][j] == 1:
            adj.append((i-1,j))
        if j-1 >= 0 and grid[i][j-1] == 1:
            adj.append((i,j-1))
        return adj

    queue = deque()
    ret = 0
    d = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                queue.append((i, j,0))
    adj = []
    while queue:
        i, j, d = queue.popleft()
        adj = get_adj(i,j)
        for r, c in adj:
           grid[r][c] = 2
           queue.append((r,c,d+1))

    for row in grid:
        if 1 in row:
            return -1
        
    return d
        
"""
TEST CASES
"""
#grid = [[2,1,1],[1,1,0],[0,1,1]]
#grid =  [[2,1,1],[0,1,1],[1,0,1]]
#grid = [[0,2]]


#m =  [[2,1,1],[1,1,0],[0,1,1]]  # --> 4
#m =  [[2,1,1],[0,1,0],[1,0,1]]  # --> -1
#m = [[0,2]]
#m = [[1,2]]
#m = [[1]]
#m = [[2,2,2,1,1]]
#m = [[0,2]]                 
m = [[1,1,2,0,2,0]]  # --> 2
#m = [[1],[1],[1],[1]]  # --> -1
#m = [[1,2,1,1,2,1,1]]  # --> 2
#m = [[2,1,1],[0,1,1],[1,0,1]]  # --> -1
#m = [[0]]  # --> 0
#m = [[2],[2],[1],[0],[1],[1]] # --> -1
#m = [[0,1],[2,0]]  # --> -1
#m = [[0,0,1,1,1,1,1,2,1]]  # --> 5


print(oranges_rotting(m))
