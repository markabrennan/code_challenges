"""
Submitted solution for Leet Code problem # 88:  Merge Sorted Array(s)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                l.append(nums2[j])
                j += 1
            else:
                l.append(nums1[i])
                i += 1
        if i < m:
            nums1[:] = l[:] + nums1[i:m]
        else:
            nums1[:] = l[:] + nums2[j:]


"""
The solution is O(n) (O(n+m)), but uses O(n+m) space.
This solution uses constant (O(1)) space.
"""

def merge(nums1, m, nums2, n):
    p = m + n -1
    i = m -1
    j = n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[p] = nums1[i]
            i -= 1
        else:
            nums1[p] = nums2[j]
            j -= 1
        p -= 1
    while j >= 0:
        nums1[p] = nums2[j]
        j -= 1
        p -= 1