"""
Leet Code 26. Remove Duplicates from Sorted Array
"""

def remove_duplicates(nums):
    seen = set()
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] in seen:
            nums.pop(i)
            j -= 1
        else:
            seen.add(nums[i])
            i += 1
    return len(nums)

"""
Another version
"""
def remove_duplicates2(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


"""
TEST CASES
"""
nums = [0,0,1,1,1,2,2,3,3,4]  # expected result:  5
#nums  = [1,1]  # expected result: 1

print(remove_duplicates2(nums))
print(nums)
