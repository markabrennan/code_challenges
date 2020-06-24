"""
Educative - Qudruple Sum to Target
"""

def search_qudruplets(arr, target):
    res = []
    seen = set()
    quads = []
    arr.sort()
    cur = []
    for i in range(len(arr)):
        sub = target - arr[i]
        lo = i + 1
        hi = len(arr) - 1
        cur.append(arr[i])
        while lo < hi:
            if arr[lo] != arr[lo-1]:
                cur.append(arr[lo])
            if len(cur) == 4 and sum(cur) == sub and tuple(sorted(cur)) not in seen:
                res.append(sub)
                seen.add(tuple(sorted(cur)))
                break
            lo += 1
    return res



"""
TEST CASES
"""

"""
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""

arr = [4, 1, 2, -1, 1, -3]
target=1

print(search_qudruplets(arr, target))