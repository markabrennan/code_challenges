"""
Leet Code Problem # 11: Container With Most Water
"""

def max_area(height):
    """
    - Two pointers (i, j) move inwards;
    - For each (i, j) pair, find the min
      value, and then multiple min * min to derive
      a new area;
    - Re-set the area using the max of previous or current
      area
    """
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        cur_height = min(height[i], height[j])
        cur_width = j - i
        cur_area = cur_height * cur_width

        max_area = max(max_area, cur_area)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return max_area




"""
TEST CASES
"""

"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

height = [1,8,6,2,5,4,8,3,7]
print(max_area(height)) 
