"""
Grokking the Coding Interview:
https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO
"""


def non_repeat_substring(s):
    start = 0
    char_set = set()
    max_len = 0
    for i in range(len(s)):
        if s[i] not in char_set:
            max_len = max(max_len, (i-start)+1)
            char_set.add(s[i])
        else:
            char_set.add(s[i])
            start = i
    return max_len



"""
TEST CASES
"""

"""
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
"""
s ="aabccbb"


"""
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
"""

"""
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""

print(non_repeat_substring(s))