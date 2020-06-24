"""
Grokking The Coding Interview: 
Longest Subarray with Ones after Replacement (hard)

"""

def longest_sub_after_replace(arr, k):
    zero_count = 0
    max_len = 0
    start = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count += 1
        if zero_count > k:
            start += 1
            zero_count -= 1
        max_len = max(max_len, i-start+1)
    return max_len
    
    
"""
TEST CASES
"""

"""
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
"""
arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k=2

print(longest_sub_after_replace(arr, k))


