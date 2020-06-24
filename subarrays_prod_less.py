"""
Educative Grokking the Coding Interview
Subarrays with product less than a target
"""

from functools import reduce
from operator import mul

"""
My version - below - works (!)
but is more verbose than the text
book version. However, it does not use
a deque; instead it uses reduce(). It
deals with the "windowing" by popping
the beginning of the contiguous array 
until the contiguous sub-array product is
less than the target.
"""

def find_subarrays2(arr, target):
    prods = [[arr[0]]]
    contig = [arr[0]]
    for i, v in enumerate(arr[1:]):
        if v < target:
            prods.append([v])
        contig_prod = reduce(mul, contig)
        if contig_prod * v < target:
            contig.append(v)
            prods.append(contig.copy())
        else:
            while contig_prod * v >= target:
                if contig:
                    contig.pop(0)
                if contig:
                    contig_prod = reduce(mul, contig)
                else:
                    break
            if contig:
                contig.append(v)
                prods.append(contig.copy())
    return prods


"""
Text book solution
"""
from collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]

        while (product >= target and left < len(arr)):
            product /= arr[left]
            left += 1

        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result
      



"""
TEST CASES
"""

"""
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
"""
# arr = [2, 5, 3, 10]
# target=30 

"""
Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
"""
arr = [8, 2, 6, 5]
target=50 

print(find_subarrays2(arr, target))
