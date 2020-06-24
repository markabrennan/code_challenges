"""
Leet Code problem "Two City Schdeduling" - # 1029

Although the code and logic are trivial, I found it hard to grok the
essence of how to minimize the cost, and tried numerous sorts
One way of thinking of this, which the solution below demonstrates,
is to sort based on the highest price differential between the two cities,
and then take the lower of the two.  However, as I had noticed earlier on,
you also have to keep track of how many times you "visit" either city A or city
B, which is done with the count variasbles below.  Not super elegant, but it works, and
makes sense intuitively.

"""

def f(l):
    sl = sorted(l, key=lambda x: abs(x[0]-x[1]), reverse=True)
    n = len(l)//2
    count_a = 0
    count_b = 0
    tot = 0
    for i, v in enumerate(sl):
        if count_a < n and count_b < n:
            if v[0] < v[1]:
                tot += v[0]
                count_a += 1
            else:
                tot += v[1]
                count_b += 1
        else:
            if count_a < n:
                tot += v[0]
                count_a += 1
            elif count_b < n:
                tot += v[1]
                count_b += 1
    return tot
