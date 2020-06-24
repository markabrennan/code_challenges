"""
New attempt at Leet Code # 42: Trapping Rain Water
"""


# def scan(i, h):
#     start = h[i]
#     local_count = 0
#     for ix in range(i+1, len(h)):
#         if h[ix] < start:
#             local_count += start - h[ix]
#         if h[ix] > start:
#             break
#     return ix, local_count


def scan(i, h):
    start = h[i]
    local_count = 0
    wall = False
    end = len(h)
    num_drops = 0
    for j in range(i+1, end):
        nxt = h[j]
        if nxt < start and j != end-1:
            local_count += start - nxt
            num_drops += 1
        if nxt > start or (nxt == start and local_count > 0): 
            wall = True
            break
        elif j == end-1 and nxt <= start-1 and local_count>0 and num_drops <=1:
            local_count -= start - nxt
            if local_count < 0:
                local_count = 0
            wall = True
            break
    if wall:
        return j, local_count
    else:
        return i+1, 0

def get_span(i, h):
    start = h[i]
    drop = False
    trap = False
    j = 0
    for j in range(i+1, len(h)):
        val = h[j]
        if val < start:
            drop = True
        if (val == start or val > start or (j==len(h)-1 and val<start)) and drop:
            trap = True
            break

    return trap, i, j

def calc_traps(i, j, h):
    # get minimimum of the edges
    edge = min(h[i], h[j])
    trap_count = 0
    for j in range(i+1, j):
        cur = min(h[j], edge)
        trap_count += edge - cur
    return trap_count




def trap(height):
    # remove first and last since no water collects there
    count = 0
    i = 0
    j = len(height)
    new_i = 0
    new_count = 0
    trap = False
    while i < j:
        if i == 0 and height[i] == 0:
            i += 1
            continue
        trap, i, j = get_span(i, height)
        if trap:
            count += calc_traps(i, j, height)
            i = j
        else:
            i += 1
        j = len(height)
        
    return count

"""
This is one of the recommended solutions, using
left and right walls and left and right pointers
"""
def trap2(height):
    left = 0
    right = len(height) - 1
    left_wall = 0
    right_wall = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_wall:
                left_wall = height[left]
            else:
                water += left_wall - height[left]
            left += 1
        else:
            if height[right] >= right_wall:
                right_wall = height[right]
            else:
                water += right_wall - height[right]
            right -= 1
    return water





"""
TEST CASE
"""

#height = [0,1,0,2,1,0,1,3,2,1,2,1]  # expected result:  6
#height = [2, 0, 2]   # expected result:  2
#height = [4, 2, 3]   # expected result:  1
#height = [5,4,1,2]   # expected result:  1
height = [4,4,4,7,1,0]  # expected result: 0
#height = [0,7,1,4,6]  # expected result: 7


print(trap2(height))