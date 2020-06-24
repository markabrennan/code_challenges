"""
Leet Code April Daily Challenge
Contiguous Array
"""

def contiguous_array(nums):
    def get_dist(nums, start):
        elem_1 = nums[start]
        if elem_1 == 0:
            elem_2 = 1
        else:
            elem_2 = 0
        e2_ix = nums.index(elem_2, start)
        d1 = e2_ix - start
        try:
            next_ix = nums.index(elem_1,e2_ix)
            d2 = next_ix - e2_ix
        except ValueError:
            d2 = d1
        if d1 != d2:
            return (-1, e2_ix)
        else:
            return d1, d2
            
    i = 0
    max_len = 0
    end = len(nums) - 1
    while i < end:
        try:
            d1, d2 = get_dist(nums, i)
        except ValueError:
            break
        if d1 == d2:
            max_len = max(max_len, d1)
            i = d1 + d2 + 1
        elif d1 == -1:
            i = d2
        else:
            i += 1
    return max_len

def f(nums):
    def get_pat(nums, start):
        zero_count = 0
        one_count = 0
        cur_elem = nums[start]
        if cur_elem == 0:
            zero_count += 1
        else:
            one_count += 1
        i = start + 1
        end = len(nums) - 1
        while i <= end:
            if nums[i] == 0 and cur_elem == 0:
                zero_count += 1
            elif nums[i] == 0 and cur_elem == 1:
                if one_count == zero_count:
                    break
                cur_elem = 0
                zero_count = 1
            elif nums[i] == 1 and cur_elem == 0:
                if one_count == zero_count:
                    break
                cur_elem = 1
                one_count = 1
            elif nums[i] == cur_elem and nums[i] == 1 and i < end:
                one_count += 1
            i += 1
        return zero_count, one_count, i
    max_len = 0
    i = 0
    end = len(nums) - 1
    while i < end:
        zero_count, one_count, ix = get_pat(nums, i)
        max_len = max(max_len, zero_count)
        i = ix
    pat = [0] * zero_count + [1] * one_count
    pat_len = len(pat)
    max_pat_len = 0
    i = 0
    while i <= end:
        if nums[i:i+pat_len] == pat:
            max_pat_len = max(max_pat_len, max_pat_len+pat_len)
            i += pat_len
        else:
            i += 1
    return max_pat_len

def contig_array2(nums):
    col = dict.fromkeys([0,1],0)
    for i in nums:
        col[i] += 1
    return col[0]*2 if col[0] < col[1] else col[1]*2

def contig_array3(nums):
    max_len = 0
    zeroes = 0
    col = dict.fromkeys([0,1],0)
    ones = 0
    for i,v in enumerate(nums):
        col[v] += 1
        if col[0] == col[1]:
            max_len = max(max_len, 2*col[0])
    if max_len == 0:
        max_len = min(col[0], col[1])*2
    return max_len
        
"""
Moving to Leet Code Solutions - 
This is the brute force approach,
which I need to learn.
Porting it from Java
"""

def findMaxLength(nums):
    maxlen = 0
    for i in range(len(nums)):
        zeroes = 0
        ones = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeroes += 1
            else:
                ones += 1
            if zeroes == ones:
                maxlen = max(maxlen, j - i + 1)

    return maxlen

"""
Leet Code Python Solution Submission
"""
def findMaxLength2(nums):
    """
    The trick is to keep a running total, in the following way:
    adding 1 for each 1, and subtracting 1 for each zero.
    Then, we keep track of the first place that total was seen (a map
    by sum of each index). The partition of that index to where we are now
    represents a subarray with equal ones and zeros.
    """
    sums = {}
    sums[0] = -1 # seed the sums map
    max_size = 0
    sum_so_far = 0
    for i, v in enumerate(nums):
        sum_so_far += 1 if v else -1
        if sum_so_far in sums:
            max_size = max(i - sums[sum_so_far], max_size)
        else:
            sums[sum_so_far] = i
    return max_size



"""
TEST CASES
"""
#nums = [0,1] # expected result: 2
#nums = [0,1,0]  # expected result: 2
#nums = [0,1,1]  # expected result:  2
#nums = [0,0,0,1,1,1,0]  # expected results:  6
#nums = [0,0,1,0,0,0,1,1] # expected results: 6  seq must be:  1,0,0,0,1,1
nums = [0,1,0,1]  # expected results: 4
#nums = [0,1,1,0,1,1,1,0]  # expected: 4

#print(contiguous_array(nums))

print(findMaxLength2(nums))
