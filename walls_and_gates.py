"""
Leet Code Problem # 286 - Walls and Gats
"""

from collections import deque

[[2147483647 ,-1, 0, 2147483647],
[2147483647, 2147483647, 2147483647 ,  -1],
[2147483647,  -1,  2147483647, -1],
[0,  -1, 2147483647, 2147483647]]

INF = 2147483647
#INF = float('inf')

def wallsAndGates(rooms):
    stack = []
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j] == INF:
                stack.append((i,j, 0))
                min_dist = get_min_dist(i, j, stack, rooms)
                rooms[i][j] = min_dist

def get_min_dist(i, j, stack, rooms):
    min_dist = INF
    visit = [[False for x in range(len(rooms[0]))] for y in range(len(rooms))]
    while stack:
        i, j, d = stack[-1]
        visit[i][j] = True
        if rooms[i][j] == 0:
            min_dist = min(d, min_dist)
            stack.pop()
            continue
        if rooms[i][j] == -1:
            stack.pop()
            continue
        if i+1 < len(rooms) and rooms[i+1][j] != -1 and visit[i+1][j] == False:
            visit[i+1][j] = True
            stack.append((i+1, j, d+1))
            continue
        if j+1 < len(rooms[i]) and rooms[i][j+1] != -1 and visit[i][j+1] == False:
            visit[i][j+1] = True
            stack.append((i, j+1, d+1))
            continue
        if i-1 >= 0 and rooms[i-1][j] != -1 and visit[i-1][j] == False:
            visit[i-1][j] = True
            stack.append((i-1, j, d+1))
            continue
        if j-1 >= 0 and rooms[i][j-1] != -1 and visit[i][j-1] == False:
            visit[i][j-1] = True
            stack.append((i, j-1, d+1))
            continue
        stack.pop()
    return min_dist



# rooms = [[2147483647 ,-1, 0, 2147483647],
# [2147483647, 2147483647, 2147483647 ,  -1],
# [2147483647,  -1,  2147483647, -1],
# [0,  -1, 2147483647, 2147483647]]

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

# rooms = [[float('inf') ,-1, 0, float('inf')],
# [float('inf'), float('inf'), float('inf') ,  -1],
# [float('inf'),  -1,  float('inf'), -1],
# [0,  -1, float('inf'), float('inf')]]

print(rooms)
wallsAndGates(rooms)
print(rooms)