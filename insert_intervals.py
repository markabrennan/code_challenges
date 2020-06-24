"""
Insert intervals
From Grokking The Coding Interview
"""


"""
Merge function taken from earlier problem;
we will re-use
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
My initial version simply re-uses the
previous merge function, relying on the sorting;
simply append the new interval to the list, relying
on the sort in merge()
"""
def insert(intervals, new_interval):
    intervals.append(new_interval)
    return merge(intervals)


"""
Another version without the second sort;
trying to improve on N log N time
"""
def insert2(intervals, new_interval):
    new_start = new_interval[0]
    new_end = new_interval[1]
    prev_start, prev_end  = intervals[0]
    i = 1
    j = len(intervals)
    while i < j:
        start, end = intervals[i]
        if prev_end < new_start < start:
            start = new_start
            end = max(end, new_end)
            intervals[i] = [start, end]
        elif prev_end < new_start > start:
            end = max(end, new_end)
            intervals[i] = [start, end]
        prev_start, prev_end  = intervals[i]
        i += 1
    return intervals
       


"""
TEST CASES
"""

"""
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
"""
# intervals = [[1,3], [5,7], [8,12]]
# new_interval = [4,6]

"""
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
"""
intervals = [[1,3], [5,7], [8,12]]
new_interval = [4,10]

"""
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""
# intervals = [[2,3],[5,7]]
# new_interval = [1, 4]



#intervals = [[1,3], [5,7], [10,12], [6,9]]
# intervals = [[1,3], [5,7], [10,12], [4,6]]
# print(merge(intervals))


print(insert2(intervals, new_interval))
