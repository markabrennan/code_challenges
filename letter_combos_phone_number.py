"""
Leet Code Problem #17:
Letter Combinations of a Phone Number

supposed to be a backtracking problem
"""


mappings = {2:['a','b', 'c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
}

print(mappings[2])

def letter_combos(digits):
    set1 = []
    set2 = []
    if len(digits) < 1:
        return []    
    if len(digits) < 2 and digits[0] == 1:
        return []

    # brute force first:
    res = []
    for i in range(len(digits)):
        st = mappings[int(digits[i])]
        print(st)
        for j in range(1, len(digits)):
            print(f'j: {j} | digits[j]: {digits[j]}')
            alt_set = mappings[int(digits[j])]
            if st != alt_set:
                for let1 in st:
                    for let2 in alt_set:
                        res.append(let1 + let2)
    return res

"""
Brute force via for loops will
not work because we don't know how
many digits will be passed in
"""
def letter_combos2(digits):
    if len(digits) < 1:
        return []    
    if len(digits) < 2 and digits[0] == 1:
        return []
    ret = []
    def letter_combo_helper(digits, pos, n, s):
        nonlocal ret
        if pos == n:
            ret.append(s)
            return

        lets = mappings[int(digits[pos])]
        for l in lets:
            letter_combo_helper(digits, pos+1, n, s+l)
            
    letter_combo_helper(digits, 0, len(digits), '')
    return ret
    


print(letter_combos2('234'))
