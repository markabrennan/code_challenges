"""
Leet Code Problem 22:  Generate Parentheses
"""

def generate_parens(n):
    res = []
    cur_perm = ''
    def dfs(s):
        if len(s) >= (2 * n) - 1:
            s += ')'
            return
        s += '()'
        dfs(s)
        res.append(s)
        s = '('
        dfs(s)
        res.append(s)
    s = ''
    dfs(s)
    return res


"""
Solution from Daniel Ni
via YouTube:  https://www.youtube.com/watch?v=LxwiwlUDOk4
Recursion and concatenation.
Managing the following state:
- current state of combinations string 
- number of opening parens available
- number of opening parens not closed
"""

def generate_parens2(n):
    if n == 0:
        return []
    return generate_parens_helper('', n, 0)

    
def generate_parens_helper(curr, num_avail, num_unclosed):
    if num_avail == 0:
        return [curr + ')' * num_unclosed]
    elif num_unclosed == 0:
        return generate_parens_helper(curr + '(', num_avail-1, num_unclosed+1)
    # we have unclosed parens, so branch two ways:
#        return generate_parens_helper(curr + '(', num_avail-1, num_unclosed+1) + generate_parens_helper(curr + ')', num_avail, num_unclosed-1)
    ret = generate_parens_helper(curr + '(', num_avail-1, num_unclosed+1)
    ret2 = ret + generate_parens_helper(curr + ')', num_avail, num_unclosed-1)
    return ret2




"""
TEST CASES
"""

print(generate_parens2(2))
