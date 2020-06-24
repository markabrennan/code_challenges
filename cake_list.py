"""
Some linked list work, based on Interview Cake 
problems and code.
"""

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None

def print_list(node):
    vals = []
    n = node
    while n:
        vals.append(n.value)
        n = n.next
    return vals

"""
This is a version I did where I copy
each node before adding to the reversed list
"""
def rev2(node):
    prev = None
    cur = node
    while cur:
        tmp = LinkedListNode(cur.value)
        tmp.next = prev
        prev = tmp
        cur = cur.next
    return prev


"""
this is the version from Interview Cake;
it does NOT copy nodes, but rather re-points
them
"""
def rev(node):
    cur = node
    prev = None
    nxt = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


print(print_list(rev2(a)))
