"""
Leet Code Problem # 15:  3Sum
"""

"""
Solution from Leet Code - used in conjunction
with 3Sum
Canonical two pointer solution:
"""

def twoSumII(numbers, target):
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while i < j:
        cur = numbers[i] + numbers[j]
        if cur == target:
            return [i + 1, j + 1]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []


"""
Canonical solution using hash map
"""

def twoSumHash(numbers, target):
    d = {}
    for i, v in enumerate(numbers):
        t = target - v
        if t in d:
            return [d[t] + 1, i + 1]
        else:
            d[v] = i
    return []    
        



def three_sum(nums):
    sl = sorted(nums)
    sol = []
    s = set()
    end = len(nums)
    for i, v in enumerate(sl):
        target = 0 - v
        j = (i + 1) % end
        k = end - 1
        while j < k:
            if sl[j] + sl[k] == target and j != i and k != i and tuple(sorted([v, sl[j], sl[k]]))  not in s:
                l = sorted([v, sl[j], sl[k]])
                sol.append(l)
                s.add(tuple(l))
                j += 1
                k -= 1
            elif sl[j] > sl[k]:
                j += 1
            else:
                k -= 1
    return sol


from collections import defaultdict

def two_sum(nums, target):
    d = defaultdict(list)
    for i, v in enumerate(nums):
        d[v].append(i)
    res = []
    for i, v in enumerate(nums):
        compliment = target - v
        
        if compliment in d and d[compliment] != i:
            return [i, d[compliment][0]]
#        if (target - v) in d and d[target-v][0] != i and len(res) != 2:
#            res.append(i)
            # if len(d[target-v]) > 1 and i == d[target-v][0]:
            #     res.append(d[target-v][1])
            # else:
            #     res.append(d[target-v][0])
#            res.append(compliment)

    return sorted(res)


def twoSum(nums, target):
    a = {}
    for i, v in enumerate(nums):
        targ = target - v
        if targ in a:
            return [a[targ], i]
        a[v] = i


def two_sum_2(nums, target):
    i = 0
    j = len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return [nums[i], nums[j]]

        elif s < target:
            i += 1
        else:
            j -= 1



def threeSum(nums):
    nums.sort()
    st = set()
    sol = []
    for i, v in enumerate(nums):
        target = 0 - v
        s = two_sum_2(nums[:i] + nums[i+1:], target)
        if s:
            s.append(v)
            if tuple(sorted(s)) not in st:
                sol.append(sorted(s))
                st.add(tuple(sorted(s)))

    return sol


def threeSum2(nums):
    def twoSum(nums, target):
        a = {}
        for i, v in enumerate(nums):
            targ = target - v
            if targ in a:
                return [a[targ], i]
            a[v] = i

    sol = []
    for i, v in enumerate(nums):
        target = 0 - v
        s = twoSum(nums[:i] + nums[i+1:], target)
        s.append(v)
        sol.append(s)
    return sol




"""
TEST CASES
Three Sum
"""

"""
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

#nums = [-1, 0, 1, 2, -1, -4]
#nums = [0,0,0]
nums = [-2,0,1,1,2]
#nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]

print(threeSum(nums))

"""
TWO SUM TEST CASES
"""

# nums = [2, 7, 11, 15]  
# target = 9  # expected:  [0,1]

# nums = [3,2,4]
# target = 6  # expected: [1,2]

# nums = [3,3]
# target = 6  # expected [0,1]

#print(two_sum(nums,target))
# print(twoSum(nums, target))



