"""
Leet Code April Daily Challenge
Last Stone Weight
"""


def last_stone_weight(stones):
    sl = sorted(stones, reverse=True)
    i = 0
    j = 1
    end = len(sl) - 1
    while len(sl) >= 2:
        zero = sl[0]
        first = sl[1]
        if zero == first:
            sl.pop(0)
            sl.pop(0)
        elif zero > first:
            new = zero - first
            sl.pop(0)
            sl.pop(0)
            sl.append(new)
            sl = sorted(sl, reverse=True)
        elif zero < first:
            new = first - zero
            sl.pop(0)
            sl.pop(0)
            sl.append(new)
            sl = sorted(sl, reverse=True)
    if len(sl) < 1:
        return 0
    return sl[0]


"""
TEST CASES
"""
stones = [2,7,4,1,8,1] # expected result:  1
"""
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""
print(last_stone_weight(stones))