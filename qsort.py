import random

def qs(l):
    if len(l) < 2:
        return l
    p = len(l) // 2
    pv = l[p]
    low = [x for x in l if x <= pv]
    hi = [x for x in l if x > pv]
    return qs(low) + [pv] + qs(hi)

def pivot(l):
        p = random.randrange(0, len(l))
        pv = l[p]
        i = 0
        j = len(l) - 1
        while i < j:
            if l[j] < pv:
                l[i], l[j] = l[j],l[i]
                i += 1
            j -= 1
        l[j], l[p], l[p], l[j]


def _qs(l, start, end):
    if start >= end:
        return
    pivot = l[random.randrange(start,end)]
    i = start
    j = end
    while i <= j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i<= j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    _qs(l, start, j)
    _qs(l, i, end)

def qs2(l):
    _qs(l, 0, len(l)-1))
           

l = [3,6,1,1,9,4,8] 

#qs(l)

pivot(l)

