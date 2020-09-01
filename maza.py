"""
Leet Code Coding Challenge
The Maze
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3432/
"""


def has_path(maze, start, destination):
    cur = start
    vmap = [[False for i in range(len(maze[0]))] for j in range(len(maze))]
    def dfs(maze, i, j, destination):
        nonlocal cur
        nonlocal vmap
        if i < 0 or i >= len(maze) or j < 0 or j >= len(maze[i]) or maze[i][j] == 1 or [i,j] == destination or vmap[i][j]:
            cur = [i,j]
            return 
        print(f'i: {i} | j: {j} | destination: {destination} | len(maze): {len(maze)} | len(maze[i]): {len(maze[i])}')
        vmap[i][j] = True
        dfs(maze, i+1, j, destination)
        dfs(maze, i, j+1, destination)
        dfs(maze, i-1, j, destination)
        dfs(maze, i, j-1, destination)

    i = start[0]
    j = start[1]
    dfs(maze, i, j, destination)

    return cur


def has_path2(maze, start, destination):
    row_len = len(maze)
    col_len = len(maze[0])
    valid = False
    vmap = [[False for i in range(col_len)] for j in range(row_len)]
    def dfs(i, j):
        nonlocal vmap, row_len, col_len, valid
        if i < 0 or i >= row_len or j < 0 or j >= col_len or vmap[i][j]:
            return
        if maze[i][j] == 1:
            vmap[i][j] = True
            return
        if [i,j] == destination:
            print('found dest')
            # check if we can pass through
            # this location - if three sides
            # are walls, we cannot
            num_sides = 0
            if (i-1 >= 0 and maze[i-1][j] == 1) or i-1 < 0:
               num_sides += 1
            if (i+1 < row_len and maze[i+1][j] == 1) or i+1 >= row_len:
               num_sides += 1
            if (j-1 <= 0 and maze[i][j-1] == 1) or j-1 < 0:
                num_sides += 1
            if (j+1 < col_len and maze[i][j+1] == 1) or j+1 >= col_len:
                num_sides += 1
            if num_sides > 2:
                valid = True
            return

        vmap[i][j] = True 
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i-1, j)
        dfs(i, j-1)

    dfs(start[0], start[1])
    return valid
    

"""
Same function but without additional checks around destination.
"""
def has_path3(maze, start, destination):
    row_len = len(maze)
    col_len = len(maze[0])
    valid = False
    vmap = [[False for i in range(col_len)] for j in range(row_len)]
    def dfs(i, j):
        nonlocal vmap, row_len, col_len, valid
        if i < 0 or i >= row_len or j < 0 or j >= col_len or vmap[i][j]:
            return
        if maze[i][j] == 1:
            vmap[i][j] = True
            return
        if [i,j] == destination:
            print('found dest')
            # check if we can pass through
            # this location - if three sides
            # are walls, we cannot
            valid = True
            return

        vmap[i][j] = True 
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i-1, j)
        dfs(i, j-1)

    dfs(start[0], start[1])
    return valid

"""
Yet another revision to my code, trying to follow
logic flow of "hasPath" below to get my code right.
"""
def has_path4(maze, start, destination):
    row_len = len(maze)
    col_len = len(maze[0])
    vmap = [[False for i in range(col_len)] for j in range(row_len)]
    def dfs(i, j):
        nonlocal vmap, row_len, col_len
        if not vmap[i][j]:
            vmap[i][j] = True
        else:
            return False
        
        if [i, j] == destination:
            return True

        down = i
        while down + 1 < row_len and maze[down+1][j] != 1:
            down += 1
        if dfs(down, j):
            return True

        right = j
        while right + 1 < col_len and maze[i][right+1] != 1:
            right += 1
        if dfs(i, right):
            return True

        up = i
        while up -1 >= 0 and maze[up-1][j] != 1:
            up -= 1
        if dfs(up, j):
            return True

        left = j
        while left - 1 >= 0 and maze[i][left-1] != 1:
            left -= 1

        if dfs(i, left):
            return True

        return False

    return dfs(start[0], start[1])

 
"""
Python version from community submissions
"""
def hasPath(maze, start, destination):
    visited = set()
    def dfs(x, y):
        if (x, y) not in visited: visited.add((x, y))
        else: return False
        
        if [x, y] == destination: return True
        
        for i, j in (0, -1), (0, 1), (-1, 0), (1, 0):
            new_x, new_y = x, y
            
            while 0 <= new_x + i < len(maze) and 0 <= new_y + j < len(maze[0]) and maze[new_x + i][new_y + j] != 1:
                new_x += i
                new_y += j
            
            if dfs(new_x, new_y): return True
        return False
    return dfs(*start)


"""
TEST CASES
"""

# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# start = [0,4]
# destination = [4,4]
"""
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
"""

# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# start = [0,4]
# destination = [3,2]

# Output: False


maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
start = [4,3]
destination = [0,1]

# output: False


print(has_path4(maze, start, destination))