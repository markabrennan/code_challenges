"""
Leet Code Problem # 937 - Reorder Data in Log Files
"""

import re


def get_logs(l):
    lets = []
    digs = []

    for i in l:
        if i.startswith('let'):
            lets.append(i)
        if i.startswith('dig'):
            digs.append(i)

    return lets, digs        



def get_reordered_lets(lets):
    i1 = r'let[0-9]* '
    i2 = r'let[0-9*]'

    intermed = [ (re.sub(i1, '', i), re.findall(i2, i)[0]) for i in lets]
    inter_sort = sorted(intermed)
    final = [ str(i[1] + ' ' + i[0]) for i in inter_sort ]

    return final


def sort_alpha(alpha):
    intermed = [(' '.join(l[1:]), l[0]) for l in alpha]
    sorted_tupes = sorted(intermed)
    return [str(i[1] + ' ' + i[0]) for i in sorted_tupes]


def parse_log(log):
    alpha = []
    digi = []
    for line in log:
        l = line.split()
        if l[1].isalpha():
            alpha.append(l)
        else:
            digi.append(l)
    return alpha, digi

        
def reorder_log_files(log):
    alpha, digi = parse_log(log)
    sorted_alpha = sort_alpha(alpha)

    sorted_alpha.extend([' '.join(l) for l in digi]) 

    return sorted_alpha


log = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

res = reorder_log_files(log)