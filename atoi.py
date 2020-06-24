"""
Leet Code Problem 8: String to Integer (atoi).
Having done some other stirng to int and int to string
conversions, I had the main formula:
    for c in num_string:
        res = res * 10 + d[c] // where d[c] is the mapping of the individual string digit to an int
But then I spent an hour working through edge cases, of which there were many!
In the end my code is not particularly efficient, but here it is:
"""

def myAtoi(self, s: str) -> int:  
        def has_dec(s):
            try:
                return s.index('.') > -1
            except:
                return False

        d = {str(i):i for i in range(0,10)}
        is_neg = False
        res = 0
        s = s.strip()
        s = s.split()
        if len(s) < 1:
            return 0
        num_string = s[0]
        if len(num_string) < 1:
            return 0
        if num_string.isalpha() or num_string[0].isalpha():
            return 0
        if len(num_string) > 1 and num_string[0] in ['+', '-']:
            if num_string[1].isalpha() or num_string[1]=='+' or num_string[1]=='-':
                return 0
        if num_string[0] == '-':
            is_neg = True
            num_string= num_string[1:]
        elif num_string[0] == '+':
            num_string= num_string[1:]
        if has_dec(num_string):
            num_string = num_string[:num_string.index('.')]
            if len(num_string) < 1:
                return 0
        found_dig = False
        for c in num_string:
            if found_dig and not c.isdecimal():
                break
            if not c.isdecimal():
                continue
            res = res * 10 + d[c]
            found_dig = True

        if is_neg:
            res = (-1) * res
        if res < (-2 ** 31):
            return -2 ** 31
        if res >= 2 ** 31:
            return (2 ** 31) - 1
        return res
