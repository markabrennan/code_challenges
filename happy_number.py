"""
Grokking the Coding Interview
Happy Number
"""


def find_happy_number(nums):
    sols = set()
    n = nums
    while True:
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        digits = digits[::-1]
        sq_sum = 0
        for i in digits:
            sq_sum += i**2
        if sq_sum == 1:
            return True
        if sq_sum in sols:
            return False
        sols.add(sq_sum)
        n = sq_sum
        



"""
TEST CASES
"""

"""
Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3^2 ​​  = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^2 + 0^2 = 1 + 0 = 1
"""


print(find_happy_number(876))



