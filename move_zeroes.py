"""
Leet Code - "Move Zeros"
"""

"""
Previous solution
"""

def move_zeroes(nums):
    for i in range(len(nums)):
        try:
            ix = nums.index(0)
            nums.append(nums.pop(ix))
        except ValueError:
            break

"""
New version - initial test case works;
but it fails test case: [0,0,1] since
1 moves to position 1 after the first pop
and append.....
"""
def move_zeroes2(nums):
    for i, v in enumerate(nums):
        if v == 0:
            nums.pop(i)
            nums.append(0)

"""
Next attempt - do swaps - oops didn't work!
Instead, use the pop() and append(), but 
decrement the end of the list to ensure we maintain
the place of non-zero integers.
Key idea is you cannot simply iterate the list, since
you are changing positions.  Instead, you maintain
pointers into the list and only increment or decrement
the pointers (one or the other) depending on whether you have a zero 
(in which case things will move down, so you maintain i where it is and decrement
j, because you've added to the ned); or you don't have a zero, so you increment i, 
while maintaining j at the last position (remember that j is initialized to the end of 
the list minus 1).

"""
def move_zeroes3(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            j -= 1
        else:
            i += 1
    
            
            


"""
TEST CASE
"""
nums = [0,1,0,3,12]
#nums = [0,0,1]

print(nums)
move_zeroes3(nums)
print(nums)
