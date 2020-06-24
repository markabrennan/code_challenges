"""
find the rotation point in a sorted list of words - from Interview Cake
"""


def f(w):
    def _f(first, w):
        print(f'first: {first} | w is : {w}')
        if len(w) == 2:
            print(f'w[0]: {w[0]} | w[1]: {w[1]}')
            
            return w[0] if w[0] < first else w[1]
        m = len(w) // 2
        l = w[0:m]
        r = w[m:]
        print(f'w: {w} *|* l: {l} *|* r: {r} *|* w[{m}]: {w[m]}')
        if w[m] < first:
            if m-1 >= 0 and w[m-1] > first:
                return w[m]
            else:
                _f(first, w[:m])
        else:
            if m+1 < len(w) and w[m+1] < first:
                return w[m]
            else:
                _f(first, w[m:])
                
    first = w[0]
    return _f(first, w[1:])


w = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']

f(w)
