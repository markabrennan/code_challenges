"""
Leet Code 387: First Unique Character in a String
I have solved this problem before, but wanted to
re-code it, given that it's a Bloomberg problem.
"""

def first_unique_char(s):
    lets = dict.fromkeys(set(s),(0,0))
    for i, v in enumerate(s):
        cnt = lets[v][0]
        cnt += 1
        lets[v] = (cnt, i)
    new_list = []
    for i in s:
        new_list.append((lets[i][0], lets[i][1], i))
    return sorted(new_list)[0][1]    


"""
This was my original code - pasting in here to save it.
Looks like I used the same approach!
"""
def firstUniqChar(self, s: str) -> int:
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



"""
TEST CASES
"""
#s = "leetcode"  # returns 0

s = "loveleetcode"  # returns 2


print(first_unique_char(s))