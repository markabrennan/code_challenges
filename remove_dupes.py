"""
Remove Duplicates In Place from a sorted list
Grokking The Coding Interview
https://www.educative.io/courses/grokking-the-coding-interview/mEEA22L5mNA
"""


def remove_dupes(arr):
    char = arr[0]
    i = 1
    j = len(arr) - 1
    while i <= j:
        if arr[i] == char:
            arr.pop(i)
            j -= 1
        else:
            char = arr[i]
            i += 1
    return len(arr)


"""
"Official" solution
"""
def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    print(f'arr[{next_non_duplicate - 1}] : {arr[next_non_duplicate - 1]}  arr[{i}]:  {arr[i]}')
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      print(f'arr[{next_non_duplicate}] : {arr[next_non_duplicate]}  arr[{i}]:  {arr[i]}')
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate


def remove_dupes2(arr, key):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == key:
            arr.pop(i)
            j -= 1
        else:
            i += 1
    return len(arr)


def remove_dupes3(arr, key):
    next_elem = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_elem] = arr[i]
            next_elem += 1
    return next_elem
    


"""
Test Caes
"""

"""
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
"""

#arr = [2, 3, 3, 3, 6, 9, 9]

"""
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""
#arr = [2, 2, 2, 11]

#print(remove_dupes(arr))
# print(remove_duplicates(arr))
# print(arr)


"""
TEST CASE for removing ALL instances of "key"
"""


"""
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
"""
arr = [3, 2, 3, 6, 3, 10, 9, 3]
key=3
print(remove_dupes3(arr, key))
print(arr)




