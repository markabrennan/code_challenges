class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def print_list(node):
    vals = []
    cur = node
    while cur:
        vals.append(cur.data) 
        cur = cur.next
    return vals

def has_cycle(node):
    fast, slow = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


"""
TEST CASES
"""
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)


n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n3

print(has_cycle(n1))
