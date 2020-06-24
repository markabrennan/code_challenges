"""
Grokking the Coding Interview
"""


def merge(intervals):
    merged = []
    intervals.sort()

    merged.append(intervals[0])

    for start, end in intervals[1:]:
        prev_start, prev_end = merged.pop()
        if start <= prev_end:
            end = max(prev_end, end)
            merged.append([prev_start, end])
        else:  
            # non-overlapping:
            # add back previous interval 
            # and add new interval
            merged.append([prev_start, prev_end])
            merged.append([start, end])

    return merged


"""
TEST CASES
"""

"""
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
"""
#intervals = [[1,4], [2,5], [7,9]]

"""
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
"""
#intervals = [[6,7], [2,4], [5,9]]

"""
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""
intervals = [[1,4], [2,6], [3,5]]

print(merge(intervals))