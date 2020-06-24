def permutations(s):
    if len(s) <= 1:
        return set(s)
    left_str = s[:-1]
    last_char = s[-1]

    perms = permutations(left_str)

    new_perms = set()
    for p in perms:
        for pos in range(len(left_str) + 1):
            perm = p[:pos] + last_char + p[pos:]
            new_perms.add(perm)

    return new_perms
    

print(permutations('cat'))
