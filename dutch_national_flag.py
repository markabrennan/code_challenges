"""
Educative - Dutch National Flag
Classic two pointer problem
"""


def dutch_flag_sort(arr):
    low = 0
    hi = len(arr) - 1
    i = 0
    while i <= hi:
        # for debug purposes, explicitly save our values
        I = arr[i]
        if I == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif I == 1:
            i += 1
        else:
            arr[i], arr[hi] = arr[hi], arr[i]
            hi -= 1

    return arr





"""
TEST CASES
"""

"""
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
"""
arr = [1, 0, 2, 1, 0]

"""
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""
#arr = [2, 2, 0, 1, 2, 0]


print(dutch_flag_sort(arr))