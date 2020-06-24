# Leet Code Problem 200 - Number of Islands

def count_islands(inp):
    num_islands = 0
    vmap = make_visit_map(inp)
    col_places = []
    for row_num, row in enumerate(inp):
        for col_num, col in enumerate(row):
            if inp[row_num][col_num] == 1 and vmap[row_num][col_num] == False:
                vmap[row_num][col_num] = True
                num_islands += 1
                col_places.append(col_num)
                new_col_places = scanrow(row[col_num+1:], row_num, col_num, vmap)
                col_places.extend(new_col_places)
                scandown(inp[row_num+1:], col_places, row_num, vmap)
            else:
                vmap[row_num][col_num] = True
                col_places = []
    return num_islands


def scanrow(row, row_num, cur_col_num, vmap):
    col_places = []
    for col_num in range(len(row)):
        vmap[row_num][col_num+cur_col_num+1] = True
        if row[col_num] == 1:
            col_places.append(col_num+cur_col_num+1)
        if row[col_num] == 0:
            return col_places
    return col_places


def scandown(matrix, col_places, cur_row_num, vmap):
    for row_num, row in enumerate(matrix):
        cur_row_col_places = []
        for col_num, col in enumerate(row):
            if col_num in col_places and matrix[row_num][col_num] == 1:
                cur_row_col_places.append(col_num)
                vmap[row_num+cur_row_num+1][col_num] = True
                new_col_places = scanrow(row[col_num+1:], cur_row_num+row_num+1, col_num, vmap)
                col_places.extend(new_col_places)
            elif col_num in col_places and matrix[row_num][col_num] == 0:
                vmap[row_num+cur_row_num+1][col_num] = True
                cur_row_col_places.extend(new_col_places)
                continue


def get_num_islands(matrix):
    vmap = make_visit_map(matrix)
    num_islands = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not vmap[i][j] and matrix[i][j] == '1':
                num_islands += 1
                vmap[i][j] = True
                # scan down this column
                c = i+1
                print(f'c is: {c}, j is: {j}, len(matrix): {len(matrix)}')
                while c < len(matrix) and matrix[c][j] == '1' and not vmap[c][j]:
                    print(f'c is: {c}, j is: {j}, len(matrix): {len(matrix)}')
                    
                    vmap[c][j] = True
                    c += 1
                # scan rest of row:
                h = j+1
                while h < len(matrix[i]) and matrix[i][h] == '1' and not vmap[i][h]:
                    vmap[i][h] = True
                    # then scan column (the same way we scanned the row):
                    c = i+1
                    print(f'c is: {c}, h is: {h}, len(matrix): {len(matrix)}')
                    while c < len(matrix) and matrix[c][h] == '1' and not vmap[c][h]:
                        print(f'c is: {c}, h is: {h}, len(matrix): {len(matrix)}')
                        vmap[c][h] = True
                        c += 1
                    h += 1
                    
    return num_islands

def visit(matrix, i, j, vmap):
    if matrix[i][j] == '0':
        return
    vmap[i][j] = True
    if i+1 < len(matrix) and not vmap[i+1][j]:
        visit(matrix, i+1, j, vmap)
    if j+1 < len(matrix[i]) and not vmap[i][j+1]:
        visit(matrix, i, j+1, vmap)
    if i-1 >= 0 and not vmap[i-1][j]:
        visit(matrix, i-1, j, vmap)
    if j-1 >= 0 and not vmap[i][j-1]:
        visit(matrix, i, j-1, vmap)


# I think this is the code for the correct solution!
def get_n5(grid):
    vmap = make_visit_map(grid)
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not vmap[i][j] and grid[i][j] == '1':
                num_islands += 1
                visit(grid, i, j, vmap)
    return num_islands



def get_n4(matrix):
    vmap = make_visit_map(matrix)
    num_islands = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not vmap[i][j] and matrix[i][j] == '1':
                num_islands += 1
                vmap[i][j] = True
                ii = i+1
                jj = j
                while ii < len(matrix) and matrix[ii][jj] == '1':
                    vmap[ii][jj] = True
                    jjj = jj+1
                    while jjj < len(matrix[ii]) and matrix[ii][jjj] == '1':
                        vmap[ii][jjj] = True
                        iii = ii-1
                        # now go back up the column
                        while iii >= 0 and matrix[iii][jjj] == '1':
                            vmap[iii][jjj] = True
                            iii -= 1
                        jjj += 1
                    ii += 1
                jj = j+1
                while jj < len(matrix[i]) and matrix[i][jj] == '1':
                    vmap[i][jj] = True
                    ii = i+1
                    jjj = jj
                    while ii < len(matrix) and matrix[ii][jjj] == '1':
                        vmap[ii][jjj] = True
                        jjjj = jjj
                        while jjjj < len(matrix[ii]) and matrix[ii][jjjj] == '1':
                            vmap[ii][jjjj] = True
                            jjjj += 1
                        # now go backwards across the row
                        jjjj = jjj
                        while jjjj >= 0 and matrix[ii][jjjj] == '1':
                            vmap[ii][jjjj] = True
                            jjjj -= 1
                        ii += 1
                    jj += 1
    return num_islands

    

def make_visit_map(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    vmap = [[False for i in range(cols)] for j in range(rows)]
    return vmap

def make_test_case0(rows=3, cols=4):
    inp = [[0 for i in range(cols)] for j in range(rows)]
    inp[0][0] = 1
    inp[0][1] = 1
    inp[0][3] = 1
    inp[1][0] = 1
    inp[2][3] = 1
    return inp

def make_test_case1(rows=4, cols=5):
    matrix = [[0 for i in range(cols)] for j in range(rows)]
    matrix[0][0] = 1
    matrix[0][1] = 1
    matrix[0][2] = 1
    matrix[0][3] = 1

    matrix[1][0] = 1
    matrix[1][1] = 1

    matrix[1][3] = 1

    matrix[2][0] = 1
    matrix[2][1] = 1

    return matrix


def make_test_case2(rows=4, cols=5):
    matrix = [[0 for i in range(cols)] for j in range(rows)]

    matrix[0][0] = 1
    matrix[0][1] = 1
    
    matrix[1][0] = 1
    matrix[1][1] = 1

    matrix[2][2] = 1

    matrix[3][3] = 1
    matrix[3][4] = 1

    return matrix


def make_test_case3():
    m = [[0 for i in range(4)] for j in range(3)]
    m[0][0] = '1'
    m[0][1] = '1'
    m[0][2] = '1'
    m[0][3] = '1'
    
    m[1][3] = '1'

    m[2][3] = '1'

    return m

if __name__ == "__main__":
#    matrix = make_test_case3()

    m1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    m3 = make_test_case3()

    m2 = [['1', '1', '1'], ['1', '0', '1'], ['1', '1', '1']]
    m4 = [["1","1","1","1"],["1","1","0","1"],["1","1","0","1"],["0","0","1","1"]]

    m5 = [["1","1","0","1"],["1","0","0","0"],["0","0","0","1"]]

    m6 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    m7 = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
    m8 = [["1","1","0","1"],["1","0","0","0"],["0","0","0","1"]]

    
    
    #n = get_num_islands(m1)
    n = get_n5(m8)

    print(n)


    # matrix = make_test_case0()
    # count_islands(matrix)



    # matrix = make_test_case2(4, 5)
    # count_islands(matrix)

