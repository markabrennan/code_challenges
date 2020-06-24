"""
Grokking the Coding Interview:
Squaring a Sorted Array
"""


def make_squares(l):
    res = [0 for x in range(len(l))]
    n = len(l)
    idx = n - 1
    i = 0
    j = idx
    while i < j:
        i_sq = l[i] ** 2
        j_sq = l[j] ** 2
        if i_sq > j_sq:
            res[idx] = i_sq
            i += 1
        else:
            res[idx] = j_sq
            j -= 1
        idx -= 1
    return res


"""
TEST CASES
"""


l = [-3, -1, 0, 1, 2]
print(make_squares(l))
