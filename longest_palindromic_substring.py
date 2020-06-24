"""
Leet Code Problem #5:  Longest Palindromic Substring
"""


"""
helper function
"""
def is_pal(s):
    length = len(s)
    mid = length // 2
    left = s[0:mid]
    if length % 2 == 0:
        right = s[mid:]
    else:
        right = s[mid+1:]
    return left == right[::-1]


def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


def longest_pal_sub2(s):
    max_pal = ''
    for i, c in enumerate(s):
        tmp1 = expand(s, i-1, i+1)
        tmp2 = expand(s, i, i+1)
        max_pal = max(max_pal, tmp1, tmp2, key=len)

    return max_pal
        


# Try iterating and building up a greedy substring
def longest_palindromic_substring(s):
    if is_pal(s):
        return s
    max_pal = ''
    temp = ''
    end = len(s)

    if len(s) == 1:
        return s
    if len(s) == 2 and s[0] != s[1]:
        return s[0]
    i = 0
    j = 1
    forw = 0
    back = 0

    while j < end:
        if s[i] == s[j]:
            # two matching chars: 
            # 1: scan forward
            forw = j + 1
            while forw < end and s[i] == s[forw]:
                forw += 1
            temp = s[i:forw]
            # 2: scan backward
            back = i 
            while back >= 0 and s[i] == s[back-1]:
                back -= 1
            temp = s[back:i] + temp

            # 3: now go both directions
            while back >= 0 and forw + 1 < end and s[back-1] == s[forw+1]:
                temp = s[back-1] + temp + s[forw]
                back -= 1
                forw += 1
            i = forw - 1
            j = i + 1
        elif j + 1 < end and s[i] == s[j+1]:
            temp = s[i:j+2]
            back = i - 1
            forw = j + 2
            while back >= 0 and forw < end and s[back] == s[forw]:
                temp = s[back] + temp + s[forw]
                back -= 1
                forw += 1
            i += 1
            j = i + 1
        else:
            i += 1
            j += 1
        max_pal = max(temp, max_pal, key=len)
        tmp = ''
    if len(max_pal) < 1:
        return s[0]

    return max_pal
            
"""
TEST CASES
"""

#s = "babad"  # "bab" - "aba" is also valid
#s = "cbbd"  # "bb"
#s = "bb"  # expected: "bb"
#s = 'ac'  # expected: "a"
#s = 'aba'  # expected:  'aba'
#s = 'xabax'  # expected: 'xabax'
s = 'fffffffffffffffffffgggggggggggggggggggg'
#s = 'ccc'   # expected: 'ccc
#s = "abcda"  # expected: "a"
#s = "abacab"  # expected: "bacab"
#s = "bananas"  # expected:  "anana"
#s = 'gdsooosgq'  # expected: "sooos"
#s = 'mqooooor'  # expected: 'ooooo'

#print(longest_palindromic_substring(s))
print(longest_pal_sub2(s))
