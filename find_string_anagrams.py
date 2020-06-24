"""
Find all string anagrams.
From Grokking the Coding Interview:
https://www.educative.io/courses/grokking-the-coding-interview/YQ8N2OZq0VM
"""


def find_string_anagrams(s, p):
    indices = []
    char_map = dict.fromkeys(set(p), 0)
    matched = 0
    start = 0
    for i in p:
        char_map[i] += 1
    for i in range(len(s)):
        ch = s[i]
        if ch in char_map:
            char_map[ch] -= 1
            if char_map[ch] == 0:
                matched += 1
        if matched == len(p):
            indices.append(start)
        if i >= len(p) - 1:
            left_char = s[start]
            start += 1
            if left_char in char_map:
                if char_map[left_char] == 0:
                    matched -= 1
                char_map[left_char] += 1

    return indices


"""
TEST CASES
"""

"""
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
"""
# s = "ppqp"
# p = "pq"

"""
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""
s = "abbcabc"
p = "abc"

print(find_string_anagrams(s, p))