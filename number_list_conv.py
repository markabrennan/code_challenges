"""
Important code to move back and
forth between integers and lists,
and vice versa.
"""

"""
Given an integer - e.g., 7809 - 
return a list of individual elements
"""
def int_to_list(n):
    res = []
    num = n
    while num:
        res.append(num % 10)
        num = num // 10
    return res[::-1]

"""
TEST CASES
"""
print(int_to_list(1234))


"""
Given a list of number elemtents,
combine into a single integer.
"""
def list_to_int(l):
    num = 0
    for i in l:
        num = num * 10 + i
    return num

"""
TEST CASES
"""
print(list_to_int([1,2,3,4]))

