"""
Leet Code "Maximum Subarray"
"""

def f(l):
    mx = l[0]
    running = l[0]
    for i in l[1:]:
        running += i
        mx = max(mx, i, running)
        running = max(i, running)
    return mx

"""
TEST CASES
"""

l = [-2,1,-3,4,-1,2,1,-5,4]  # expected result:  [4,-1,2,1] has the largest sum = 6

print(f(l))