"""
Leet Code "easy" problem to detect first occurrence
of a unique character and return its position.
My solution uses a dict to track occurrences and each
character's position in the array.
"""
def first_unique_char(s):
    sl = list(s)
    l = dict.fromkeys(sl, (0,0))
    for ix, c in enumerate(sl):
        count = l.get(c, 0)[0]
        l[c] = (count+1, ix)
    singles = []
    for k, v in l.items():
        if v[0] == 1:
            singles.append(v)
    if len(singles) < 1:
        return -1
    return sorted(singles)[0][1]



print(first_unique_char('cc'))