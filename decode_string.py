"""
Leet Code Problem # 394: Decode String
Tricky string parsing requiring a stack.
(Perhaps recursion would work as well.)
"""


def decode_string(s):
    nums = []
    lets = []
    cur = ''
    tmp = ''
    full = ''
    for i in s:
        if i.isnumeric():
            nums.append(int(i))
            # clear cur to start the next stack "frame"
            cur = ''
            if len(tmp) > 0:
                lets.append(tmp)
                tmp = ''
        if i.isalpha():
            tmp += i
        if i == ']':
            if len(tmp) > 0:
                lets.append(tmp)
                tmp = ''
            # pop one number; pop letters
            num = nums.pop()
            let = lets.pop()
            print(f'num is: {num} | letters: {let} | cur: {cur}')
            # build up string:
            cur += num * (let + cur)
            full += cur
            print(f'cur is now: {cur}')
            
    return full


def rec_decode_string(s):
    def recurse(i, s1):
        tmp = ''
        cur = ''
        num = 0
        num_str = ''
        end = len(s1)-1
        while i <= end:
            if s1[i].isnumeric():
                num_str += s1[i]
            if s1[i].isalpha():
                tmp += s1[i]
            if s1[i] == '[':
                num = int(num_str)
                num_str = ''
                i, cur = recurse(i+1, s1)
                cur = num * cur
                tmp += cur
                i += 1
                continue
            if i < end and s1[i] == ']':
                return i, tmp
            i += 1
        return i, tmp

    i = 0
    end = len(s)-1
    tmp = ''
    cur = ''
    num = 0
    num_str = ''
    while i <= end:
            if s[i].isnumeric():
                num_str +=s[i]
            if s[i].isalpha():
                tmp += s[i]
            if s[i] == '[':
                num = int(num_str)
                num_str = ''
                i, cur = recurse(i+1, s)
                cur = num * cur
                tmp += cur
            i = i+1

    return tmp


def recursive_decode_string(S):
    def recurse(s):
        cur = ''
        tmp = ''
        num = 0
        num_str = ''
        i = 0
        j = len(s)-1

        while i < j:
            if s[i].isnumeric():
                num_str += s[i]
            elif s[i].isalpha():
                cur += s[i]
            elif s[i] == '[':
                num = int(num_str)
                num_str = ''
                i, tmp = recurse(s[i+1:])
                cur += cur + (num * tmp)
            elif s[i] == ']':
#                return i, cur
                pass
            i += 1

        return i, cur
    
    _, res = recurse(S)
    return res


"""
TEST CASES
"""

s = "3[a]2[bc]"    # return "aaabcbc"
#s = "3[a2[c]]"     # return "accaccacc"
#s = "2[abc]3[cd]ef" # return "abcabccdcdcdef"
#s = "100[leetcode]"  # return leetcodeX100 !
#s = "3[a]2[b4[F]c]"  # return "aaabFFFFcbFFFFc"
#s = "3[a10[bc]]"  # return "abcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbc"


# res = rec_decode_string(s)
# print(res)


print(recursive_decode_string(s))