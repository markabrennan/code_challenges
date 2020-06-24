"""
Leet Code April Daily Challenge
Middle of Linked List
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Helper function - I use this
to print out the elements
of the linked list
"""
def print_list(node):
    vals = []
    cur = node
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals

"""
First version
"""

def middle_node(head):
    node_map = {}
    cur = head
    index = 0
    while cur:
        node_map[index] = cur
        cur = cur.next
        index += 1
    mid = len(node_map) // 2
    return node_map[mid]

"""
Another version without incurring extra space;
however, I don't see any other way to do it
except with two passes.
"""
def middle_node2(head):
    index = 0
    cur = head
    while cur:
        index += 1
        cur = cur.next
    mid = index // 2
    index = 0
    cur = head
    while cur:
        if index == mid:
            return cur
        index += 1
        cur = cur.next

"""
And this is Steven Kaneti's version,
which I think is more elegant, as well
as being more concise.
"""
import math

def middle_node3(head):
    counter = 0
    cnode = head
    mid = head
    while cnode is not None:
        counter += 1
        cnode = cnode.next
    for j in range(math.floor(counter / 2)):
        mid = mid.next
    return mid
    
    
    
"""
TEST CASES
"""
#input list: [1,2,3,4,5]  # expected output:  [3,4,5]
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# a.next = b
# b.next = c
# c.next = d
# d.next = e

#input list: [1,2,3,4,5]  # expected output:  [4, 5, 6]
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# f = ListNode(6)

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

#input list:  [65,66,26,77,96,86,11,21,13,80]  # expected output:  ??
a = ListNode(65)
b = ListNode(66)
c = ListNode(26)
d = ListNode(77)
e = ListNode(96)
f = ListNode(86)
g = ListNode(11)
h = ListNode(21)
i = ListNode(13)
j = ListNode(80)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j
#print(print_list(a))

print(print_list(middle_node3(a)))
