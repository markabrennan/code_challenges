"""
Linked List Cycle - fast and slow pointers
from Grokking the Coding Interview
https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D
"""

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

    
def count_cycle(head):
    fast = slow = head
    count = 0
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            # start count:
            count += 1
            runner = fast.next
            while runner != slow:
                count += 1
                runner = runner.next
            return count
    return count

def find_cycle_start(head):
    cycle_len = count_cycle(head)
    p1 = p2 = head
    for i in range(cycle_len):
        p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1.value
    

def find_middle_of_linked_list(head):
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    mid = len(nodes) // 2
    return nodes[mid]

"""
This is the official solution
using fast and slow pointers
"""
def find_middle_of_linked_list2(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def print_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.value)
        cur = cur.next
    return vals


def remove_nth_from_end(head, n):
    dummy = Node()
    dummy.next = head
    first = second = dummy
    for i in range(n):
        first = first.next
    while first and first.next:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

def is_palindrome_linked_list(head):
    # find middle first:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow is in the middle now
    rev_head = reverse(slow)
    cur = head
    while rev_head and rev_head.next:
        if cur.value != rev_head.value:
            return False
        rev_head = rev_head.next
        cur = cur.next
    return True


    # cur = head
    # rev_cur = rev_head
    # while cur and rev_cur:


def reverse(head):
    prev = nxt = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

"""
Official solution from Grokking The Coding Interview
for reversed sub_list
"""
def reverse_sub_list(head, p, q):
    if p == q:
        return head
    # after skipping 'p-1' nodes, current will point to 'p'th node
    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1
    # we are interested in three parts of the LinkedList, the part before index 'p',
    # the part between 'p' and 'q', and the part after index 'q'
    last_node_of_first_part = previous
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None  # will be used to temporarily store the next node
    i = 0
    # reverse nodes between 'p' and 'q'
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
    # connect with the first part
    if last_node_of_first_part is not None:
        # 'previous' is now the first node of the sub-list
        last_node_of_first_part.next = previous
    # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
    else:
        head = previous
    # connect with the last part
    last_node_of_sub_list.next = current
    return head


"""
same version, different variable naming, based on my own code
"""
def rev_sub_list2(head, p, q):
    i = 0
    prev = nxt = None
    cur = head
    p_minus_node = None
    p_plus_node = None
    while cur and i < p-1:
        prev = cur
        cur = cur.next
        i += 1
    p_minus_node = prev
    p_plus_node = cur
    i = 0
    while cur and i < q - p + 1:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        i += 1
    if p_minus_node is not None:
        p_minus_node.next = prev
    else:
        head = prev
    p_plus_node.next = cur
    return head


def rev_sublist(head, p, q):
    prev = nxt = None
    cur = p_minus = head
    q_plus = None
    cnt = 1
    end = 1
    while cur:
        nxt = cur.next
        if cnt == p and cnt != q:
            q_plus = cur.next
            cur.next = prev
            prev = cur
        else:
            if prev is not None:
                prev.next = cur
            else:
                prev = cur
                prev.next = None
            last = cur
        cur = nxt
        cnt += 1
    return prev

def reorder(head):
    print(print_list(head))
    # find middle of list:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow points to middle - reverse it:
    rev_head = reverse(slow)
    print(print_list(rev_head))
    # iterate from head and thread in nodes from
    # reversed second half
    cur = head
    while cur and rev_head:
        tmp = cur.next
        cur.next = rev_head
        cur = tmp

        tmp = rev_head.next
        rev_head.next = cur
        rev_head = tmp

    if cur is not None:
        cur.next = None

    return head
        

"""
TEST CASES
"""

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)
# head.next.next.next.next.next.next = Node(7)

# cycle
#head.next.next.next.next.next.next = head.next.next

# print(has_cycle(head))
# print(count_cycle(head))
#print(find_cycle_start(head))

#print(find_middle_of_linked_list2(head).value)

# head = Node(2)
# head.next = Node(4)
# head.next.next = Node(6)
# head.next.next.next = Node(8)
# head.next.next.next.next = Node(10)
# head.next.next.next.next.next = Node(12)

# print(print_list(head))
# print(print_list(remove_nth_from_end(head, 2)))
#print(print_list(reorder(head)))

# test case for reversed sub_list
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(print_list(n1))

print(print_list(rev_sub_list2(n1, 2,4)))