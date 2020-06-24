"""
Leet Code Problem # 70:  Word Search
"""

def make_visit_map(board):
    rows = len(board)
    cols = len(board[0])
    return [[False for i in range(cols)] for j in range(rows)]


def exist(board, word):
    vmap = make_visit_map(board)
    num_rows = len(board)
    num_cols = len(board[0])
    word_len = len(word)
    cur_pos = 0
    cur_word = ''
    def dfs(row, col):
        nonlocal vmap
        nonlocal cur_pos
        nonlocal cur_word
        # Logic:
        # given first letter and starting place:
        # traverse:
        # mark cur row and col as visited;
        # if cur place (row, col) is not next letter,
        # or cur place (row, col) is next letter but
        # not adjacent:  RESTART
        # else: continue with next letter
        # if row > num_rows or row < 0 or col > num_cols or col < 0:
        #     return
        # if vmap[row][col]:
        #     return
        # else:
        #     vmap[row][col] = True
        print(f'row: {row} | col: {col} | cur_pos: {cur_pos} | word: {word}')
        if row+1 < num_rows:
            print(f'letter at next row:  {board[row+1][col]}')
        if col+1 < num_cols:
            print(f'letter at next col:  {board[row][col+1]}')
        if row-1 >= 0:
            print(f'letter at prev row:  {board[row-1][col]}')
        if col-1 >= 0:
            print(f'letter at prev col:  {board[row][col-1]}')
       
        if row + 1 < num_rows and cur_pos+1 < word_len and not vmap[row+1][col] and board[row+1][col] == word[cur_pos+1]:
            cur_word += board[row+1][col]
            cur_pos += 1
            vmap[row+1][col] = True
            dfs(row+1, col)
        if col + 1 < num_cols and cur_pos+1 < word_len and not vmap[row][col+1] and board[row][col+1] == word[cur_pos+1]:
            cur_word += board[row][col+1]
            cur_pos += 1
            vmap[row][col+1] = True
            dfs(row, col+1)
        if row - 1 >= 0 and cur_pos+1 < word_len and not vmap[row-1][col] and board[row-1][col] == word[cur_pos+1]:
            cur_word += board[row-1][col]
            cur_pos += 1
            vmap[row-1][col] = True
            dfs(row-1, col)
        if col - 1 >= 0 and cur_pos+1 < word_len and not vmap[row][col-1] and board[row][col-1] == word[cur_pos+1]:
            cur_word += board[row][col-1]
            cur_pos += 1
            vmap[row][col-1] = True
            dfs(row, col-1)
        if cur_word == word:
            return

    for i in range(num_rows):
        for j in range(num_cols):
            if not vmap[i][j] and board[i][j] == word[0]:
                cur_word += board[i][j]
                dfs(i, j)
                if cur_word == word:
                    return True
                # resert cur_pos for next loop
                cur_pos = 0
                cur_word = ''
    return False


def exist_clean(board, word):
    num_rows = len(board)
    num_cols = len(board[0])
    word_len = len(word)
    vmap = [[False for i in range(num_cols)] for j in range(num_rows)]     
    cur_pos = 0
    cur_word = ''
    def dfs(row, col):
        nonlocal vmap
        nonlocal cur_pos
        nonlocal cur_word
        print(f'cur_word: {cur_word}')
        if row + 1 < num_rows and cur_pos+1 < word_len and not vmap[row+1][col] and board[row+1][col] == word[cur_pos+1]:
            save_word = cur_word
            save_pos = cur_pos
            cur_word += board[row+1][col]
            cur_pos += 1
            vmap[row+1][col] = True
            dfs(row+1, col)
            # if cur_word != word:
            #     # have to back track
            #     cur_word = save_word
            #     cur_pos = save_pos
        if col + 1 < num_cols and cur_pos+1 < word_len and not vmap[row][col+1] and board[row][col+1] == word[cur_pos+1]:
            save_word = cur_word
            save_pos = cur_pos
            cur_word += board[row][col+1]
            cur_pos += 1
            vmap[row][col+1] = True
            dfs(row, col+1)
            # if cur_word != word:
            #     # have to back track
            #     cur_word = save_word
            #     cur_pos = save_pos

        if row - 1 >= 0 and cur_pos+1 < word_len and not vmap[row-1][col] and board[row-1][col] == word[cur_pos+1]:
            save_word = cur_word
            save_pos = cur_pos
            cur_word += board[row-1][col]
            cur_pos += 1
            vmap[row-1][col] = True
            dfs(row-1, col)
            # if cur_word != word:
            #     # have to back track
            #     cur_word = save_word
            #     cur_pos = save_pos
        if col - 1 >= 0 and cur_pos+1 < word_len and not vmap[row][col-1] and board[row][col-1] == word[cur_pos+1]:
            save_word = cur_word
            save_pos = cur_pos
            cur_word += board[row][col-1]
            cur_pos += 1
            vmap[row][col-1] = True
            dfs(row, col-1)
            # if cur_word != word:
            #     # have to back track
            #     cur_word = save_word
            #     cur_pos = save_pos
        if cur_word == word:
            return

    for i in range(num_rows):
        for j in range(num_cols):
            if not vmap[i][j] and board[i][j] == word[0]:
                cur_word += board[i][j]
                vmap[i][j] = True
                dfs(i, j)
                if cur_word == word:
                    return True
                # resert cur_pos for next loop
                cur_pos = 0
                cur_word = ''
                vmap = [[False for i in range(num_cols)] for j in range(num_rows)]     
    return False


def exist2(board, word):
    rows = len(board)
    cols = len(board[0])
    word_len = len(word)
    vmap = [[False for i in range(cols)] for j in range(rows)]
    pos = 0

    def dfs(i, j):
        nonlocal pos
        nonlocal rows
        nonlocal cols
        nonlocal vmap
        if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[pos] or vmap[i][j]:
            return
        cur_vmap = vmap
        cur_pos = pos

        vmap[i][j] = True
        cur_pos = pos
        pos += 1
        dfs(i+1, j)
        dfs(i, j+1)
        dfs(i-1, j)
        dfs(i, j-1)
        if pos != word_len:
            vmap = cur_vmap
            pos = cur_pos



    for i in range(rows):
        for j in range(cols):
            if not vmap[i][j] and board[i][j] == word[0]:
                dfs(i, j)
                if pos == word_len:
                    return True
                else:
                    pos = 0
                    vmap = [[False for i in range(cols)] for j in range(rows)]
    return False                    

"""
Kevin Naughton's solution
https://www.youtube.com/watch?v=vYYNp0Jrdv0&t=113s
For some reason I didn't know how to "chain" my recurisve
calls.  His solution uses an OR conditon to see if 
successive calls work (return True) but resets
the given cell's value each time via tmp.
My problem appears to be that I was trhing to code a base case
in the recursive call, but did not evalute its "truth",
which is the way you allow the recursive to continue.
This is what allows for BACKTRACKING, which I was struggling with.
"""
def exist3(board, word):
    def dfs(board, i, j, count, word):
        if count == len(word):
            return True
        if i >= len(board) or i < 0 or j >= len(board[i]) or j < 0 or board[i][j] != word[count]:
            return False

        tmp = board[i][j]
        board[i][j] = ' '
        ret_val = dfs(board, i+1, j, count+1, word) or dfs(board, i, j+1, count+1, word) or dfs(board, i-1, j, count+1, word) or dfs(board, i, j-1, count+1, word)
        board[i][j] = tmp
        return ret_val
        

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                return True
    return False
               
            



"""
Test Cases
"""

# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

"""
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

board = [["a","a"]]
word = 'aaa'

"""
Word:  "aaa"
expect: False
"""


# board = [["C","A","A"],["A","A","A"],["B","C","D"]]
# word = 'AAB'
# Given word "AAB", return True


# board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# word = "ABCESEEEFS"  # expects:  True

print(exist3(board, word))