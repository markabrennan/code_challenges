"""
Another attempt (having seen the solution)
at the Leet Code 'Walls and Gates' problem.
"""


def walls_and_gates(rooms):
    def recurse(i, j, d):
        #if i >= len(rooms) or i < 0 or j >= len(rooms[i]) or j < 0 or rooms[i][j] == -1:
        if not (0 <= i < len(rooms)) or not (0<= j < len(rooms[0])) or rooms[i][j] < d:
            return
        rooms[i][j] = min(d, rooms[i][j])
        recurse(i+1, j, d+1)
        recurse(i, j+1, d+1)
        recurse(i-1, j, d+1)
        recurse(i, j-1, d+1)
        

    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            # if we reach a gate, recurse out to rooms
            if rooms[i][j] == 0:
                recurse(i, j, 0)
    return rooms 

"""
This is a solution from a Leet Code submitter
"""
def wallsAndGates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """
    def dfs(rooms, i, j, d):
        if not (0 <= i < len(rooms)) or not (0<= j < len(rooms[0])) or rooms[i][j] < d:
            return
        
        rooms[i][j] = min(d, rooms[i][j])
        dfs(rooms, i + 1, j, d + 1)
        dfs(rooms, i - 1, j, d + 1)
        dfs(rooms, i, j + 1, d + 1)
        dfs(rooms, i, j - 1, d + 1)
        
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                dfs(rooms, i, j, 0)
    return rooms

"""
TEST CASES
"""

# Input 1:
"""
INF, -1, 0, INF
INF, INF, INF, -1
INF, -1, INF, -1
0, -1, INF, INF

Where INF = 2 ** 31 -1
"""

INF = (2**31)-1
rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]

#print('BEFORE:')
#print(rooms)
print(walls_and_gates(rooms))
#print(wallsAndGates(rooms))
#print('AFTER')
#print(rooms)
