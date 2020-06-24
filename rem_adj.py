"""
Leet Code problem: "Remove All Adjacent Duplicates in a String" - # 1047
"""
from collections import defaultdict

def f(s):
    seen = defaultdict(list)
    for i, v in enumerate(s):
        if v not in seen:
            # finished adding adjacent characters
            # so remove what's in seen:
            if len(seen.items()) > 0:
                _, indices = seen.popitem()
                if len(indices) > 1:
                    begin = indices[0]
                    end = indices[-1]
                    s = s[0:begin] + s[end+1:]
                else:
                    seen.clear()
            
            seen[v].append(i)
        else:
            seen[v].append(i)

    # handle case of 'aaaaaaaa'
    if len(seen.items()) > 0:
        _, indices = seen.popitem()
        if len(indices) > 1:
            begin = indices[0]
            end = indices[-1]
            s = s[0:begin] + s[end+1:]
    
    return s

def f1(S):
    seen = ''
    for i, v, in enumerate(S):
        if v == seen:
            # delete cur char and one before:
            S = S[0:i-1] + S[i+1:]
            seen = ''
            return f1(S)
        else:
            seen = v
    return S
        


#s = 'abbbaca'
s = "aaaaaaaa"
ret = f(s)
print(ret)