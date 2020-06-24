"""
Grokking The Coding Interview:
Triplets Sum to Zero
"""

"""
Going to use a "two sum" algo for helping
"""
def two_sum(l, target):
    i = 0
    j = len(l) - 1
    while i < j:
        cur = l[i] + l[j]
        if cur == target:
            return [l[i], l[j]]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []


def two_sum2(l, i, triplets):
    left = i + 1
    right = len(l) - 1
    while left < right:
        cur = l[i]
        cur_sum = cur + l[left] + l[right]
        if cur_sum < 0 or (left > i + 1 and l[left] == l[left-1]):
            left += 1
        elif cur_sum > 0 or (right < len(l)-1 and l[right] == l[right+1]):
            right -= 1
        else:
            triplets.append([cur, l[left], l[right]])
            left += 1
            right -= 1



def search_triplets(arr):
    triplets = []
    arr.sort()
    for i, v in enumerate(arr):
        if v > 0:
            break
        if i > 0 and arr[i] == arr[i-1]:
            continue
        two_sum2(arr, i, triplets)
    return triplets


"""
TEST CASES
"""

l = [-3, 0, 1, 2, -1, 1, -2]
print(search_triplets(l))


