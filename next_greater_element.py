"""
Leet Code Problem 496: Next Greater Element

Couple of ways to solve it; reason for my doing it
was I wanted to work with stacks more and internalize
their pattern.  However, my first solution didn't
use a stack - though it was quite slow!
I subsequently did a slightly different version
with a hash map, which is only a bit faster.
"""

"""
First version
"""

def next_greater_elem(nums1, nums2):
    res = []
    for i, v in enumerate(nums1):
        mx = None
        for elem in nums2[nums2.index(v):]:
            print(f'l1 elem: {v} | l2 elem: {elem}')
            if elem > v and mx is None:
                mx = elem
        if mx is not None:
            res.append(mx)
        else:
            res.append(-1)
    return res


"""
Next version - use a map
"""

def next_greater_elem2(nums1, nums2):
    res = []
    hash = {v:i for i, v in enumerate(nums2)}
    for i in nums1:
        pos = hash[i]
        val = -1
        for j in nums2[pos:]:
            if j > i and val == -1:
                val = j
        res.append(val)
    return res


"""
Not the official solution using
a stack, but one version in the comments.
"""
def nextGreaterElement(nums1, nums2):
    stack = []
    #  create a dictionary to hold results
    res = {}
    for last_item in nums2[::-1]:

        for s in stack[::-1]:
            if s<last_item:
                stack.pop()                        
            else:
                stack.append(last_item)
                res[last_item] = s
                break
        if not stack:
            stack.append(last_item)
            res[last_item] = -1        
    return [res[i] for i in nums1]
    

"""
Another version using stack - 
this one appears to mirror the official
(Java) stack solution.
"""
def nextGreaterElement2(nums1, nums2):
    mem = {}
    stack = []
    for i in nums2:
        while stack and i > stack[-1]:
            mem[stack.pop()] = i
        stack.append(i)
    while len(stack):
        mem[stack.pop()] = -1
    return [mem[i] for i in nums1]


"""
TEST CASES
"""

#nums1 = [4,1,2] 
#nums2 = [1,3,4,2]  # expected output:  [-1,3,-1]

nums1 = [2,4]
nums2 = [1,2,3,4]  # expected output:   [3,-1]

print(nextGreaterElement2(nums1, nums2))


