"""
HackerRank Problem:  "New Year Chaos"
"""

"""
Code from original solution
"""

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        try:
            val = q[i]
            nxt = q[i+1]
            slot = i+1
            off = 0
            if val > nxt:
                off = val - nxt
                if off > 2:
                    print('Too chaotic')
                    return
                bribes += off
                # see if value may have been pushed up, in which
                # case we'd need to add another offset
                if val < slot:
                    bribes += slot-val
        except IndexError:
            continue
    print(bribes)

"""
New attempt - I think I must be missing
some edge cases given how simple this code is
"""

def f(l):
    print(f'l: {l}')
    bribes = 0
    for i in range(len(l)):
        print(f'i is: {i+1} | l[i]: {l[i]}')
        if l[i] > i+1:
            b = l[i] - (i+1)
            print(f'diff is: {b}')
            if b <= 2:
                bribes += b
            else:
                return 'Too chaotic'
    return bribes