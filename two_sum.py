"""
Gonna try Leet Code "Two Sum" problem
again, which I know can be solved with a hash
map, or with two pointers. I'd like to get both.
"""

def two_sum(nums, target):
        d = dict.fromkeys(nums, 0)
        for i, v in enumerate(nums):
            d[v] = i
        for i, v in enumerate(nums):
            diff = target - v
            if diff in d and d[diff] != i:
                return [i, d[diff]]        
        return []
"""
Trying it with two pointers.
"""
def f1(nums, target):
    num_tupes = []
    for i, v in enumerate(nums):
        num_tupes.append((v, i))
    num_tupes.sort()
    print(nums)
    print(num_tupes)
    i = 0
    j = len(nums) - 1
    while i < j:
        I = num_tupes[i][0]
        J = num_tupes[j][0]
        if I + J == target:
            return [num_tupes[i][1], num_tupes[j][1]]
        elif I + J < target:
            i += 1
        else:
            j -= 1
    return []

"""
TEST CASES
"""
# return indices of the two numbers in the
# array that add up to the target:

# [2, 7, 11, 15], target=9
# answer:  [0,1]

# nums = [2, 7, 11, 15]
# target = 9

nums = [3, 2, 4]
target = 6

print(f1(nums, target))