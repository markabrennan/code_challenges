"""
Leet Code Valid Parentheses String
"""

def valid_parens_string(s):
    pstack = []
    astack = []
    for i in s:
        if i == '*':
            astack.append(i)
        elif i == '(':
            pstack.append(i)
        elif i == ')':
            if pstack and pstack[-1] == '(':
                pstack.pop()
            elif astack and astack[-1] == '*':
                astack.pop()
            else:
                return False
    return len(pstack) == len(astack) < 2
    
"""
Leet Code Solution - Greedy
"""
def checkValidString(s):
    lo = hi = 0
    for c in s:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0: break
        lo = max(lo, 0)

    return lo == 0    
            

"""
TEST CASESS
"""
#Input = "()"
# Output: True

#Input = "(*)"
#Output: True

#Input = "(*))"
#Output: True

#Input = "(*()"
#Expected output:  True

#Input = ')'
#Expected output:  False

Input = "(((******))"
#expected output:  True

#print(valid_parens_string(Input))
print(checkValidString(Input))


