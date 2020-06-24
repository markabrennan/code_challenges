"""
From Grokking The Coding Interview
"""

def triplet_sum_close_to_target(arr, target):
    triplets = []
    for i in range(len(arr)):
       if i > 0 and arr[i] == arr[i-1]:
           continue
       sub(arr, i, target, triplets)
    triplets.sort()
    return triplets[0][1]



def sub(arr, i, target, triplets):
    left = i + 1
    right = len(arr) - 1
    while left < right:
        cur = l[i] + l[left] + l[right]
        diff = abs(target - cur)

        triplets.append((diff, cur, [l[i], l[left], l[right]]))
        if cur < target or (left > i + 1 and l[left] == l[left-1]):
           left += 1
        elif cur > target or (right < len(l)-1 and l[right] == l[right+1]):
            right -= 1
        else:
            left += 1
            right -= 1
    return triplets


"""
TEST CASES
"""

# l =  [-2, 0, 1, 2]
# target = 2

l =  [-3, -1, 1, 2]
target = 1

# l =  [1, 0, 1, 1]
# target=100


print(triplet_sum_close_to_target(l, target))