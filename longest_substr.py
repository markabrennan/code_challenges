"""
Leet Code Problem # 3:  Longest Substring Without Repeating Characters
I seem to have solved this problem before, but wanted to revisit it, and
came up with another solution (not completely vetted yet).
In order to test it on Leet Code, I need to overwrite my original solution,
and so wanted to save it here.
"""

# original solution
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) < 1:
        return 0
    subs = []
    length = len(s)
    seen = set()

    for i in range(length): 
        seen.add(s[i])
        j = i+1
        while j < length and s[j] not in seen:
            seen.add(s[j])
            j += 1

        subs.append(s[i:j])
        seen.clear()

    longest = sorted(subs, key=len, reverse=True)[0]
    return len(longest)

def f(s):
    if len(s) < 1:
        return 0
    if len(s) == 1:
        return 1    
    seen = set()
    sub = []
    all_subs = []
    longest = 0
    for i, c in enumerate(s):
        if c not in seen:
            seen.add(c)
            sub.append(c)
        else:
            all_subs.append(''.join(sub))

           # longest = max(longest, len(subs))
            seen.clear()
            sub.clear()

            if (s[i-1] != c):
                sub.append(s[i-1])
                seen.add(s[i-1])
            seen.add(c)
            sub.append(c)
    # check longest once again:
    all_subs.append(''.join(sub))
    print(f'all_subs: {all_subs}')

    return len(sorted(all_subs, key=len, reverse=True)[0])


# This solution works!  But it's very slow, since it continually
# backtracks to scan another substring.
def f1(s):
    seen = {}
    sub = []
    all_subs = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] not in seen:
            seen[s[i]] = i
            sub.append(s[i])
            i += 1
        else:
            all_subs.append(''.join(sub))
            prev_place = seen[s[i]] + 1
            seen.clear()
            sub.clear()
            i = prev_place
    all_subs.append(''.join(sub))
    print(f'all_subs: {all_subs}')
    return len(sorted(all_subs, key=len, reverse=True)[0])


""" And this is the optimal solution, adapated
from the Java code in the Leet Code Solution
"""

def f_window(s):
    n = len(s)
    seen = set()
    i = j = ans = 0
    while i < n and j < n:
        if s[j] not in seen:
            seen.add(s[j])
            print(f'cur substr: {s[i:j+1]} | cur max: {ans}')
            ans = max(ans, len(s[i:j+1]))
            j += 1
        else:
            seen.remove(s[i])
            i += 1
            
    print(f'cur substr: {s[i:j+1]} | cur max: {ans}')
    return ans


#s = 'abcabcbb'
#s = 'au'
#s = "dvdf" # Output should be 3!  ('vdf')
#s = "abcabcbb" # Expected output: 3
#s = "bbbbb" # Expected output is: 1

s = "anviaj"  # Expected output is:  5

print(f_window(s))



#print(f(s))