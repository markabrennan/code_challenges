"""
Leet Code Problem 242: Valid Anagram
I first tried sets but then realized I needed
to match letter counts in both strings, so I used
two dictionaries.  This solution was accepted.


Turns out the "official" solution uses sorting:
if both strings are sorted, they must be equivalent.
This yields n log n, whereas I believe that using the
dictionaries, while using n space, is nevertheless linear.

Finally, the alternate solution below uses a single
dict, but two passes, one each over s and t.

"""


def is_ana(s, t):
    if len(s) != len(t):
        return False
    
    flag = True
    s_dict = dict.fromkeys(s,0)
    t_dict = dict.fromkeys(t,0)
    for i in s:
        s_dict[i] += 1
    for i in t:
        t_dict[i] += 1
    for k, v in t_dict.items():
        if v != s_dict.get(k, 0):
            return False
    return True

def is_ana2(s, t)
      char_count = {}

      for char in s: 
          char_count[char] = char_count.get(char, 0) + 1
      for char in t: 
          char_count[char] = char_count.get(char, 0) - 1

     return False not in [char_count[char] == 0 for char in char_count]


"""
TEST CASES
"""

#s = "anagram" 
#t = "nagaram"  # expected output:  True

# s = 'cat'
# t = 'car'   # expected output:  False

s = "aacc"
t = "ccac"  # expected output:  False


print(is_ana(s, t))

