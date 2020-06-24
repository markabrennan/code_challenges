from collections import deque

def orangesRotting(grid):
    minutes = 0

    def fresh(grid):
        for row in grid:
            if 1 in row:
                return True
        return False    

    def visit(i, j, grid):
        nonlocal minutes
        print(f'i: {i} | j: {j}')
        print(f'grid[{i}]:  {grid[i]}')
        print(f'grid[{i}][{j}]: {grid[i][j]}')

        if i+1 >= len(grid) or grid[i+1][j] != 1:
            return

        grid[i+1][j] = 2

        if j+1 >= len(grid[i]) or grid[i][j+1] != 1:
            return
            
        grid[i][j+1] = 2

        if minutes == -1:
            minutes = 0

        minutes += 1

        visit(i+1, j, grid)
        visit(i, j+1, grid)

        minutes += 1


    # def make_rotten(i, j, grid):
    #     nonlocal minutes
    #     print(f'i: {i} | j: {j}')
    #     print(f'grid[{i}]:  {grid[i]}')
    #     print(f'grid[{i}][{j}]: {grid[i][j]}')

    #     if grid[i][j] == 0:
    #         return

    #     if grid[i][j] == 1:
    #         grid[i][j] = 2
    #         minutes += 1
    #         return

    #     if i+1 < len(grid):
    #         make_rotten(i+1, j, grid)
    #     if j+1 < len(grid[i]):
    #         make_rotten(i, j+1, grid)
    #     if i-1 >= 0:
    #         make_rotten(i-1, j, grid)
    #     if j-1 >= 0:
    #         make_rotten(i, j-1, grid)


    def make_rotten(i, j, grid):
        nonlocal minutes
        rotten = False
        if i+1 < len(grid) and grid[i+1][j] == 1:
            grid[i+1][j] = 2
            rotten = True
            make_rotten(i+1, j, grid)
        if j+1 < len(grid[i]) and grid[i][j+1] == 1:
            grid[i][j+1] = 2
            rotten = True
            make_rotten(i, j+1, grid)
        if i-1 >= 0 and grid[i-1][j] == 1:
            grid[i-1][j] = 2
            rotten = True
            make_rotten(i-1, j, grid)
        if j-1 >= 0 and grid[i][j-1] == 1:
            grid[i][j-1] = 2
            rotten = True
            make_rotten(i, j-1, grid)
        if rotten:
            minutes += 1

            
    def make_rotten2(i, j, grid):
        nonlocal minutes
        rotten = False
        visit = []
        if i+1 < len(grid) and grid[i+1][j] == 1:
            grid[i+1][j] = 2
            visit.append((i+1, j))
            rotten = True
        if j+1 < len(grid[i]) and grid[i][j+1] == 1:
            grid[i][j+1] = 2
            visit.append((i, j+1))
            rotten = True
        if i-1 >= 0 and grid[i-1][j] == 1:
            grid[i-1][j] = 2
            visit.append((i-1, j))
            rotten = True
        if j-1 >= 0 and grid[i][j-1] == 1:
            grid[i][j-1] = 2
            visit.append((i, j-1))
            rotten = True
        if rotten:
            minutes += 1

        for elems in visit:
            make_rotten2(elems[0], elems[1], grid)

        # if i+1 < len(grid) and grid[i+1][j] == 2:
        #    make_rotten2(i+1, j, grid)
        # if j+1 < len(grid[i]) and grid[i][j+1] == 2:
        #     make_rotten2(i, j+1, grid)
        # if i-1 >= 0 and grid[i-1][j] == 2:
        #     make_rotten2(i-1, j, grid)
        # if j-1 >= 0 and grid[i][j-1] == 2:
        #     make_rotten2(i, j-1, grid)
        
        
    def get_entry(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    return i, j
        return -1, -1


    def make_rotten3(grid):
        minutes = 0
        adjacent = deque()
        for i in len(grid):
            for j in len(grid[i]):
                if grid[i][j] == 1:
                    new_min, adj = rot(i, j, grid)


    # def get_neighbors(i, j, grid):
    #     neighbors = []
    #     if i + 1 < len(grid) and grid[i+1][j] == 1:
    #         neighbors.append((i + 1, j))
    #     if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
    #         neighbors.append((i, j + 1))
    #     if i - 1 >= 0 and grid[i-1][j] == 1:
    #         neighbors.append((i - 1, j))
    #     if j - 1 >= 0 and grid[i][j-1] == 1:
    #         neighbors.append((i, j - 1))

    #     return neighbors

    def get_adjacent(cells, grid):
        adjacent = []
        for cell in cells:
            i = cell[0]
            j = cell[1]
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                adjacent.append((i + 1, j))
            if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                adjacent.append((i, j + 1))
            if i - 1 >= 0 and grid[i-1][j] == 1:
                adjacent.append((i - 1, j))
            if j - 1 >= 0 and grid[i][j-1] == 1:
                adjacent.append((i, j - 1))

        return adjacent






    def visit(i, j, grid):
        nonlocal minutes
        cells = [(i,j)]
        adjacent = get_adjacent(cells, grid)
        if len(adjacent) > 0:
            while True:
                rot(adjacent, grid)
                minutes += 1
                adjacent = get_adjacent(adjacent, grid)
                if len(adjacent) == 0:
                    break

    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         # if grid[i][j] == 1:
    #         #     if is_trapped(i, j, grid):
    #         #         return -1
    #         if grid[i][j] == 0:
    #             continue
    #         if grid[i][j] == 2:
    #             adj = get_adjacent([(i,j)], grid)
    #             if len(adj) > 0:
    #                 visit(i,j, grid)
    
    # for row in grid:
    #     if 1 in row:
    #         return -1
    
    def has_adjacent(i, j, grid):
        adjacent = False
        if i + 1 < len(grid) and grid[i+1][j] == 2:
            adjacent = True
        if j + 1 < len(grid[i]) and grid[i][j+1] == 2:
            adjacent = True
        if i - 1 >= 0 and grid[i-1][j] == 2:
            adjacent = True
        if j - 1 >= 0 and grid[i][j-1] == 2:
            adjacent = True
        return adjacent

    def is_trapped(i, j, grid):
        trapped = True
        if i + 1 < len(grid) and grid[i+1][j] != 0:
            trapped = False
        if j + 1 < len(grid[i]) and grid[i][j+1] != 0:
            trapped = False
        if i - 1 >= 0 and grid[i-1][j] != 0:
            trapped = False
        if j - 1 >= 0 and grid[i][j-1] != 0:
            trapped = False
        return trapped

    def rot(cells, grid):
        nonlocal minutes
        for cell in cells:
            i = cell[0]
            j = cell[1]
            grid[i][j] = 2
        minutes += 1 
        cells.clear()

    # new start:
    rot_q = []
    fresh = is_rot = False
    while True:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    is_rot = True
                if grid[i][j] == 1:
                    fresh = True
                    if has_adjacent(i, j, grid):
                        rot_q.append((i,j))
#                    elif is_trapped(i, j, grid):
#                    elif (len(rot_q) == 0 and is_rot) or is_trapped(i,j, grid):
#                        return -1
        if len(rot_q) == 0 and not is_rot and fresh:
            return -1
        if len(rot_q) == 0:
            break
        rot(rot_q, grid)
    
    for row in grid:
        if 1 in row:
            return -1
    return minutes

#    i, j = get_entry(grid)
#    make_rotten2(i, j, grid)
#    if i > -1 and j > -1:
#        visit(i, j, grid)




    # if not fresh(grid):
    #     return 0

    # if grid[0][0] == 1:
    #     grid[0][0] = 2
        
    #     if minutes == -1:
    #         minutes = 0
    #     minutes += 1

    # visit(0, 0, grid)
    # return minutes


m =  [[2,1,1],[1,1,0],[0,1,1]]  # --> 4
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


minutes = orangesRotting(m)
print(minutes)