"""
Grokking the Coding Interview:
Permutation in a String:
https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D

"""


def find_permutation(s, p):
    start = 0
    for i in range(len(s)):
        if s[i] not in p:
            start += 1
        elif s[start] in p and s[i] in p and i - start + 1 == len(p):
            return True
    return False



"""
TEST CASES
"""

"""
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
"""

# s = "oidbcaf"
# p = "abc"

"""
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
"""
# s = "odicf"
# p = "dc"

"""
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
"""
# s = "bcdxabcdy"
# p = "bcdyabcdx"

"""
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

s = "aaacb"
p = "abc"


print(find_permutation(s, p))