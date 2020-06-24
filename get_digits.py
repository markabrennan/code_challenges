"""
Code to extract individual digits from
an integer. I wanted to formalize this
code, since I kept forgetting the precise
steps.
"""

def get_digits(n):
    nums = []
    rem = n
    while rem:
        nums.append(rem % 10)
        rem = rem // 10
    return nums[::-1]


"""
TEST CASE
"""

print(f'number: {1234} | digits: {get_digits(1234)}')
print(f'number: {9} | digits: {get_digits(9)}')
print(f'number: {19} | digits: {get_digits(19)}')
print(f'number: {109401} | digits: {get_digits(109401)}')