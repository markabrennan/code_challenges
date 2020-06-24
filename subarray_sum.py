"""
Leet Code April 30 Day Coding Challenge
Subarray Sum Equals K
"""

def sub_array_sum(nums, k):
    begin = 0
    end = 0
    cum = 0
    num_sums = 0
    i = 0 
    j = len(nums)
    while i < j:
#    for pos, i in enumerate(nums):
        if nums[i] + cum == k:
            num_sums += 1
            cum = 0
            if begin + 1 < i:
                i = begin + 1
                begin = i
        elif nums[i] == k:
            num_sums += 1
            cum = 0
            begin = i
            i += 1
        #elif nums[i] + cum > k or nums[i] + cum < 0:
        elif nums[i] + cum > k:
            cum = 0
            i += 1
            begin = i
        else:
            cum += nums[i]
            i += 1

    return num_sums



"""
TEST CASES
"""
# sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. 

# nums = [1,1,1]
# k = 2
# Output: 2

# nums = [1,2,3]
# k = 3
# output: 2

nums = [-1,-1,1]
k = 0
# output: 1


# nums = [100,1,2,3,4]
# k = 6
# output: 1


# nums = [1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2]
# k = 6
# output 5


# nums = [3,1,2,1,1,1,1,1]
# k = 6
# output = 3

print(sub_array_sum(nums, k))


