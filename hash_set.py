"""
Leet Code August Challenge:  Design a Hash Set
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/
"""

class MyHashSet:
    """
    Per problem statement, the constraint is:
    All values will be in the range of [0, 1000000]
    Therefore, let's build a sparse array.

    This is a VERY NAIVE version!  See LeetCode
    answer below for "correct" solution.
    """
    def __init__(self):
        self.sparse_array = [None] * 1000000

    def add(self, key):
        self.sparse_array[key] = 1

    def remove(self, key):
        self.sparse_array[key] = None

    def contains(self, key):
        if self.sparse_array[key]:
            return True
        else:
            return False


class MyHashSet():
    """
    Leet Code solution: s
    https://leetcode.com/problems/design-hashset/solution/
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



"""
TEST CASES
"""


hashSet = MyHashSet()
print('hashSet.add(1)', hashSet.add(1))
print('hashSet.add(2)', hashSet.add(2))
print('hashSet.contains(1)', hashSet.contains(1))    # returns true
print('hashSet.contains(3)', hashSet.contains(3))    # returns false (not found)
print('hashSet.add(2)', hashSet.add(2))
print('hashSet.contains(2)', hashSet.contains(2))    # returns true
print('hashSet.remove(2)', hashSet.remove(2))          
print('hashSet.contains(2)', hashSet.contains(2))    # returns false (already removed)