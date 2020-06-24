# Leet Code Problem 53 - Maximum Subarray
#
# First attempt - O(N^2) - too expensive; logically correct, but it times out!

 def maxSubArray(self, nums: List[int]) -> int:
        sm = None        
        if len(nums) < 0:
            return None
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)):
            subl = []
            subl.append(nums[i])
            if sm is None:
                sm = sum(subl)
            else:
                sm = max(sum(subl), sm)
    
            for j in range(i+1, len(nums)):
                subl.append(nums[j])
                subl_sum = sum(subl)
                if sm is None:
                    sm = subl_sum
                sm = max(sum(subl), sm)

        return sm


#
# Attempt # 2:
#
# Try to find the largest number in the list, and then slice from there
# Linear time

def max3(l):
    sl = sorted(l, reverse=True)
    mx = sl[0]
    ix = l.index(mx)
    subl = l[ix:]
    sm = sum(subl)
    j = len(l)
    for i in range(ix, len(l)):
        subl[:] = l[ix:j]
        sm = max(sum(subl), sm)
        j -= 1
    for i in range(0, ix): 
        subl[:] = l[i:ix+1] 
        sm = max(sum(subl), sm)        
    return sm


def max4(l):
    if len(l) < 0:
        return None
    if len(l) == 1:
        return l[0]
    mx = l[0]
    mx_ix = 0
    subl = []
    for i in range(1, len(l)):
        subl[:] = l[mx_ix:i+1]
        if l[i] > sum(subl) and l[i] > mx:
            mx_ix = i
            mx = l[i]
        else:
            mx = max(sum(subl), mx)
    return mx