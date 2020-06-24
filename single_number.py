"""
Leet Code # 136: Single Number (easy)
I previously solved it using a dictionary, but
the April 2020 Leet Code 30 Day Challenge version
asks if we can do it without using extra memory.
To do so, I believe, you need a sorted list first, 
which would then technially be n log n.
"""

def f(l):
    seen = None
    done = False
    sl = sorted(l)
    for ix, i in enumerate(sl):
        if seen is None: 
            seen = i
            done = False
        elif i == seen:
            seen = None
            done = True
        elif seen is not None and not done:
            return sl[ix-1]
    
    
    if seen is not None and not done:
        return sl[-1]


"""
This was an earlier version - my first, submited and
accepted 

"""
TEST CASES
"""
l = [4,1,2,1,2]  # expected result:  4

print(f(l))