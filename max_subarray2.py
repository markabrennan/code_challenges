"""
Max subarray problem from
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
"""

"""
I believe I previously solved this
on Leet Code, thought with some help from
Steven.  Idea is to keep track of the
running sum.
"""

def find_max_subarray(k, arr):
    max_sum = 0
    running = 0
    cur_cum = 0
    start = i = 0
    j = len(arr)

    while i < j:
        cur_cum =+ arr[i]
        if i >= k:
        #    cur_cum = cur_cum + arr[i]
            max_sum = max(max_sum, cur_cum, arr[i])
            i = start + 1
            start = i
            cur_sum = 0
        else:
            i += 1
    return max_sum


def find_max_subarray2(k, arr):
    start = 0
    max_sum = 0
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= arr[start]
            start += 1
    return max_sum


def find_min_subarray(s, arr):
    min_len = len(arr)
    running = 0
    start = 0
    for i in range(len(arr)):
        running += arr[i]
        if running >= s:
            min_len = min(i-start+1, min_len)
            print(f'min len: {min_len}')
            running -= arr[start]
            start += 1
            if running >= s:
                min_len = min(i-start+1, min_len)
                print(f'min len: {min_len}')
                running -= arr[start]
                start += 1
    return min_len


def find_min_subarray2(s, arr):
    min_len = len(arr)
    running = 0
    start = 0
    for i in range(len(arr)):
        running += arr[i]
        while running >= s:
            min_len = min(i-start+1, min_len)
            running -= arr[start]
            start += 1
    return min_len


import math

def find_max(nums):
    running = 0
    max_sum = -1 * math.inf
    for i in nums:
        running += i
        max_sum = max(max_sum, running, i)
        running = max(running, i)
    return max_sum

"""Old code from my Leet Code solution:
        if len(nums) < 0:
            return None
        if len(nums) == 1:
            return nums[0]
        
        mx = nums[0]
        running = nums[0]

        for i in range(1, len(nums)):
            running += nums[i]
            mx = max(mx, max(running, nums[i]))       
            running = max(nums[i], running)
        return mx
"""        

"""
TEST CASE for max sub array:
"""
#arr = [-2,1,-3,4,-1,2,1,-5,4]  # result:  6
arr = [-2,-1]  # result:  -1

print(find_max(arr))

"""
TEST CASES
"""
"""
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""
# arr = [2, 1, 5, 1, 3, 2]
# k = 3 
# print(find_max_subarray2(k, arr))



"""
Test case for min subarray:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
"""
s = 7
arr = [2, 1, 5, 2, 3, 2]

"""
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
"""
# s = 7
# arr = [2, 1, 5, 2, 8]

"""
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""

# s = 8
# arr = [3, 4, 1, 1, 6]

print(find_min_subarray2(s, arr))
