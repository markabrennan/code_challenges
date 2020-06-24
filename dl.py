"""
Experimenting with doubly-linked lists
"""

class Node:
    def __init__(self, val=None, next=None, prev=None, child=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

def add_node_start(head, node_val):
    new_node = Node(val=node_val)
    new_node.next = head
    head.prev = new_node
    head = new_node
    return head


def add_node_end(head, node_val):
    new_node = Node(val=node_val)
    n = head
    while n.next:
        n = n.next
    n.next = new_node
    new_node.prev = n

    return head

def print_list(head):
    elems = []
    n = head
    while n:
        elems.append(n.val)
        n = n.next
    return elems


def flatten(head):
    def _flatten(head, ret_list):
        add_node_end(ret_list, head.val)
        if head.child is not None:
            _flatten(head.child, ret_list)
        if head.next is not None:
            _flatten(head.next, ret_list)
        return ret_list
        
    ret_list = Node()
    if head is None:
        return ret
    ret_list = _flatten(head, ret_list)
    return ret_list.next

def print_flat(head):
    def _print_flat(head):
        nonlocal ret
        ret.append(head.val)
        if head.child is not None:
            _flatten(head.child)
        if head.next is not None:
            _flatten(head.next)

    ret = []
    if head is None:
        return ret

    _print_flat(head)
    return ret

"""
Leet Code solution:
"""
def flatten1(head):
    def flatten_dfs(prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = flatten_dfs(curr, curr.child)
        curr.child = None
        return flatten_dfs(tail, tempNext)
        
    if not head:
        return head

    # pseudo head to ensure the `prev` pointer is never none
    pseudoHead = Node(None, None, head, None)
    flatten_dfs(pseudoHead, head)

    # detach the pseudo head from the real head
    pseudoHead.next.prev = None
    return pseudoHead.next

"""
Cleaner version - in my own code (from memoory)
"""
def flatten3(node):
    def _flatten(prev, cur):
        if cur is None:
            return prev
        cur.prev = prev
        prev.next = cur
        tmp = cur.next
        tail = _flatten(cur, cur.child)
        cur.child = None
        return _flatten(tail, tmp)
    pseudo_head = Node(val=None, next=None, prev=node, child=None)
    _flatten(pseudo_head, node)
    pseudo_head.next.prev = None
    return pseudo_head.next



# l = Node(5)
# l.next = Node(4)
# l.next.next = Node(7)
# print(print_list(l))

# l = add_node_start(l, 9)
# print(print_list(l))

# l = add_node_end(l, 22)
# print(print_list(l))

# ch2 = Node(11)
# ch2.next = Node(12)

# ch1 = Node(7)
# ch1.next = Node(8,child=ch2)
# ch1.next.next = Node(9)
# ch1.next.next.next = Node(10)

# c1 = Node(4)
# l = Node(1)
# l.next = Node(2)
# #l.next.next = Node(3)

# l.next.next = Node(3,child=ch1)
# l.next.next.next = Node(4)
# l.next.next.next.next = Node(5)
# l.next.next.next.next.next = Node(6)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(7)
e = Node(8)
f = Node(9)
ff = Node(10)
g = Node(11)
h = Node(12)
i = Node(4)
j = Node(5)
k = Node(6)


a.next = b
b.next = c
c.child = d
d.next = e
e.next = f
f.next = ff
e.child = g
g.next = h
c.next = i
i.next = j
j.next = k


fl = flatten3(a)
print(print_list(fl))


