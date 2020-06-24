"""
Leet Code Problem # 266:  Palindorme Permutation
Determine if a permutation of a string is a valid
palindrome.

For this problem I cribbed the permuation recursive 
function from Interview Cake, which I think is an excellent
pattern, both for recursion, and for string manipulation.
"""

def perm(s):
    if len(s) <= 1:
        return set(s[0])
    left = s[:-1]
    last = s[-1]
    
    perms = perm(left)
    permutations = set()
    
    for char_perms in perms:
        for pos in range(len(left) +1):
            new_perm = char_perms[:pos] + last + char_perms[pos:]
            permutations.add(new_perm)

    return permutations
    
def is_pal(s):
    length = len(s)
    mid = length // 2
    left = s[:mid]
    if length % 2 == 0:
        right = s[mid:]
    else:
        right = s[mid+1:]
    return left == right[::-1]


def can_permute_palindrome(s):
    permutations = perm(s)
    for p in permutations:
        if is_pal(p):
            return True
    return False



"""
Better solution, based on reading the Leet Code
solution:  based on the rule that a palindrome
can consist of even number of characters or, at
most, one odd character, we can use a map.
"""
def can_perm_pal2(s):
    letter_map = dict.fromkeys(s, 0)
    for i in s:
        letter_map[i] += 1
    count = 0
    for k, v in letter_map.items():
        count += v % 2 
    return count <= 1

       

"""
TEST CASES
"""

s = "code"  # result:  False
#s = "aab"  # result:  True
#s = "carerac" # result:  True
#s = "ivicc"  # result:  True

#print(can_permute_palindrome(s))
print(can_perm_pal2(s))





