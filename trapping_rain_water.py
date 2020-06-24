"""
Leet Code Problem # 42 - Trapping Rain Water
"""


def find_range(bars):
    l = h = 0
    start = end = max_height = 0
    start_set = end_set = False
    print(bars)
    for i in range(0, len(bars)):
        nx = 0
        if i+1 < len(bars):
            nx = i+1
        print(f'start: {bars[start]} | end: {max_height} | bars[i]: {bars[i]} | bars[i+1]: {bars[nx]}')
        if i+1 < len(bars) and bars[i] > bars[i+1]:
            if not start_set:
                start = i
                start_set = True
                continue
            if bars[i] >= bars[start] and bars[i] < max_height:
                # this means we are going down after setting the start and max height
                break
            else:
                continue
        if i+1 < len(bars) and bars[i] < bars[i+1] and start_set: 
            if bars[i+1] > max_height:
                max_height = bars[i+1]
                end = i+1
                continue
    print(f'start bar: {bars[start]} - end bar: {bars[end]}')
    return ((bars[start]<=bars[end]), start, end)


def get_height(bars):
    h = 0
    prev = bars[0]
    for i in range(1, len(bars)):
        if bars[i] < prev:
            h += prev - bars[i]
    return h


def find_bars(bars):
    start = None
    start_val = None
    end = None
    end_vale = None
    for ix, bar in enumerate(bars):
        if start is None and bar > 0:
            start = ix
            start_val = bar
            continue
        if start is not None and bar >= start_val:
            end = ix
            end_val = bar
            break
    return ( bool(start is not None and end is not None), start, end)


def get_h(bars):
    start = bars[0]
    end = bars[-1]
    height = 0
    offset = 0
    if start > end:
        offset = start - end
    for i in range(1, len(bars)-1):
        print(f'start val: {start} | bars[i]: {bars[i]} | height: {height}')
        height += start - bars[i] - offset
        print(f'height is now: {height}')
    return height


def get_traps(bars):
    start = end = None
    start_val = None
    dip = 0
    for ix, bar in enumerate(bars):
        if start is None and bar > 0:
            start = ix
            start_val = bar
            continue
        if start is not None and end is None:
            if bar < start_val:
                dip = min(dip, bar)
                continue
        if start is not None and bar > dip and bar >= start_val:
            end = ix
            break
    if end is None and bars[-1] > dip:
        end = len(bars)
    return ( (start is not None and end is not None), start, end)


def find_edge(bars):
    start = bars[0]
    dip = None
    end = None
    provisional = None
    for i in range(1, len(bars)):
        print(f'start: {start} | dip: {dip} | bars[{i}]: {bars[i]}')
        if dip is None and bars[i] < start:
            dip = bars[i]
            continue
        if bars[i] < start and bars[i] <= bars[i-1]:
            dip = min(bars[i], dip)
            continue
        if bars[i] >= start:
            end = i
            break
        if bars[i] > dip and bars[i] < start:
            print('here')
            provisional = i
    print(f'dip: {dip} - provisional: {provisional}')
    if end is not None:
        return (True, 0, end)
    elif provisional is not None:
        return (True, 0, provisional)
    else:
        return (False, 0, 0)



def scan_for_traps(bars):
    i = 0
    j = len(bars)
    trapped_water = 0
    begin = end = beg_off = end_off  = 0
    while i < j:
        print(f'range is {i} - {j}')
        #trapped, beg_off, end_off = find_bars(bars[i:j])
        trapped, beg_off, end_off = get_traps(bars[i:j])
        print(f'trapped: {trapped} - begin: {beg_off} - end: {end_off}')
        if trapped:
            #begin = beg_off + end - (1 if begin != 0 else 0)
            begin = beg_off + i
            end = i + end_off + 1
            print(f'getting height for range: {bars[begin:end]}')
            #height = get_height(bars[begin:end])
            height = get_h(bars[begin:end])
            print(f'height is: {height}')
            trapped_water += height
            i = end - 1
        else:
            i += 1
            
    return trapped_water



# bars = [0,1,0,2,1,0,1,3,2,1,2,1]    
# #bars = [2, 0, 2]    
# #bars = [4,2,3]
# scan_for_traps(bars)

def permutations(string, step=0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        print("".join(string))

    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [c for c in string]
        # swap the current index with the step 
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the stringthat has not been swapped yet
        permutations(string_copy, step + 1)


# Hannah's permutation function
# class Solution:
def permute(nums):
    if len(nums) == 1:
        return [nums]
    
    elif len(nums) == 2:
        return [[nums[0], nums[1]], [nums[1], nums[0]]]
    
    else:
        permutations = []
        # n!/n ways to start with each number
        for num in nums:
            curr_nums = nums.copy()
            curr_nums.pop(nums.index(num))
            for perms in permute(curr_nums):
                permutations.append([num] + perms)
    
        return permutations
        


print (permutations ('abcd'))
l = ['a','b','c', 'd']
permute(l)

