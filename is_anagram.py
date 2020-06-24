"""
Is a string an anagram
- I somehow remembered how to do this!
"""

def ana(s):
    def rev(s):
        sl = [c for c in s]
        i = 0
        j = len(s)-1
        while i < j:
            sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1
        return ''.join(sl)

    is_odd = True
    if len(s) % 2 == 0:
        is_odd = False
        
    mid = len(s) // 2
    first = s[0:mid]
    if is_odd:
        last = s[mid+1:]
    else:
        last = s[mid:]
    rlast = rev(last)
    print(f'first: {first} | rlast: {rlast}')
    return first == rlast
