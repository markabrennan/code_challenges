"""
Leet Code April Daily Challenge
Perform String Shifts

Key is to know which way to go, since
each direction works differently
"""


def string_shift(s, shift):
    ln = len(s)
    for dir, amt in shift:
        if dir == 0:
            # left
            s = s[amt:] + s[:amt]
        else:
            # right
            s = s[ln-amt:] + s[:ln-amt]
                
    return s


"""
TEST CASES
"""

#s = "abc" 
#shift = [[0,1],[1,2]]
"""
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
"""

s = "abcdefg" 
shift = [[1,1],[1,1],[0,2],[1,3]]
"""
 Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 """

print(string_shift(s, shift))