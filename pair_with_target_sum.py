"""
Pair with target sum
Two Pointer Pattern
from Grokking the Coding Interview
https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP
"""

def pair_with_target_sum(arr, target):
    i = 0
    j = len(arr) - 1
    indices = []
    while i < j:
        if arr[i] + arr[j] > target:
            j -= 1
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            indices.append(i)
            indices.append(j)
            break
            
    return indices


"""
TEST CASES
"""

"""
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
"""

# arr = [1, 2, 3, 4, 6]
# target = 6

"""
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""
arr = [2, 5, 9, 11]
target=11

print(pair_with_target_sum(arr, target))