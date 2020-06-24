"""
Interview Cake - Recursive String Permuations
"""


# Hannah's permutation function
# class Solution:
def permute(nums):
    if len(nums) == 1:
        return [nums]
    
    elif len(nums) == 2:
        return [[nums[0], nums[1]], [nums[1], nums[0]]]
    
    else:
        permutations = []
        # n!/n ways to start with each number
        for num in nums:
            curr_nums = nums.copy()
            curr_nums.pop(nums.index(num))
            for perms in permute(curr_nums):
                permutations.append([num] + perms)
    
        return permutations
        


def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[:position]
                + last_char
                + permutation_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations


#s = 'cat'
s = "ivicc"
print(get_permutations(s))

#ar = ['c', 'a', 't']
#print(permute(ar))