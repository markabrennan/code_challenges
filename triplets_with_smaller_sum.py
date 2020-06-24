"""
Grokking the Coding Interview:
Triplets with smaller sum.  Two pointer pattern.
https://www.educative.io/courses/grokking-the-coding-interview/mElknO5OKBO
"""

def triplet_with_smaller_sum(arr, target):
    triples = []
    arr.sort()
    for i in range(len(arr)):
        # skip dupes
        if i > 0 and arr[i] == arr[i-1]:
            continue
        if i == 0:
            ii = i + 1
        else:
            ii = 0
        j = len(arr) - 1
        while ii < j and ii != i:
            new_sum = arr[i] + arr[ii] + arr[j]
            if new_sum < target:
                triples.append((arr[i], arr[ii], arr[j]))
            j -= 1
    return len(triples), triples


def triplets_with_smaller_sum2(arr, target):
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        new_target = target - arr[i]
        sub(arr, i, new_target, triplets)
    return triplets


def sub(arr, i, target, triplets):
    left = i + 1
    right = len(arr) - 1
    while left < right:
        cur = arr[left] + arr[right]
        if cur < target:
            triplets.append([arr[i], arr[left], arr[right]])
            r = right - 1
            while r > left:
                triplets.append([arr[i], arr[left], arr[r]])
                r -= 1
            left += 1
        elif cur > target:
            right -= 1
        elif cur == target:
            left += 1
            right -= 1


"""
TEST CASES
"""

"""
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
"""
# arr =  [-1, 0, 2, 3]
# target = 3 

"""
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""

arr =  [-1, 4, 2, 1, 3]
target=5 

print(triplets_with_smaller_sum2(arr, target))
