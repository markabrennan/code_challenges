"""
Leet Code 445. Add Two Numbers II
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(node):
    res = []
    cur = node
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

"""
Brute force approach
"""
def add_two_numbers(l1, l2):
    l1_nums = []
    l2_nums = []
    cur = l1
    while cur:
        l1_nums.append(cur.val)
        cur = cur.next
    cur = l2
    while cur:
        l2_nums.append(cur.val)
        cur = cur.next
    l1_int = 0
    for i in l1_nums:
        l1_int = l1_int * 10 + i
    l2_int = 0
    for i in l2_nums:
        l2_int = l2_int * 10 + i
    l_sum = l1_int + l2_int
    l_sum_list = []
    if l_sum == 0:
        return ListNode(0)
    while l_sum:
        l_sum_list.append(l_sum % 10)
        l_sum //= 10
    l_sum_list[:] = l_sum_list[::-1]
    new_node = ListNode(l_sum_list[0])
    cur = new_node
    for i in l_sum_list[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return new_node


"""
Second attempt - trying to do one pass
"""
def add_two_numbers2(l1, l2):
    def get_list_len(node):
        cur = node
        ln = 0
        while cur:
            ln += 1
            cur = cur.next
        return ln
    l1_len = get_list_len(l1)
    l2_len = get_list_len(l2)
    if l1_len >= l2_len:
        start = l1
        follow = l2
        start_len = l1_len
        follow_len = l2_len
    else:
        start = l2
        follow = l1
        start_len = l2_len
        follow_len = l1_len
    summation = 0
    carry = None
    tens = 0
    extra = 0
    cur = start
    cur_follow = follow
    new_cur = new_list_head = ListNode(None)
    sync = False
   # while cur and cur_follow:
    for i in range(start_len):
        if start_len - i == follow_len or start_len == follow_len or sync:
            sync = True
            cur_sum = cur.val + cur_follow.val
            if cur.next and cur_follow.next and cur.next.val + cur_follow.next.val >= 10:
                extra = cur.next.val+cur_follow.next.val - 10 + 1

            if carry and cur_sum >= 10:
                new_val = carry
                carry = cur_sum - 10
            elif carry and cur_sum < 10:
                new_val = cur_sum
            elif carry < 1 and cur_sum < 10:
                new_val = cur_sum + extra
            elif carry < 1 and cur_sum >= 10:
                carry = cur_sum - 10
                new_val = 0 + extra
            new_cur.next = ListNode(new_val)
            cur = cur.next
            cur_follow = cur_follow.next
            new_cur = new_cur.next
            extra = 0
        else:
            new_cur.next = ListNode(cur.val)
            cur = cur.next
            new_cur = new_cur.next
    if carry:
        # we need an extra node:
        new_cur.next = ListNode(carry)
    return new_list_head.next

"""
Leet Code Submission
"""

def addTwoNumbers(l1, l2):
    def insert_begin(head, val):
        node = ListNode(val)
        if head:
            node.next = head
            head = node
        else:
            head = node
        return head

    l1_stack = []
    l2_stack = []

    head = None
    carry = 0

    while l1 or l2:
        if l1:
            l1_stack.append(l1.val)
            l1 = l1.next
        if l2:
            l2_stack.append(l2.val)
            l2 = l2.next

    while l1_stack or l2_stack:
        top1 = l1_stack.pop() if l1_stack else 0
        top2 = l2_stack.pop() if l2_stack else 0
        res = top1 + top2 + carry
        carry = res//10
        head = insert_begin(head, res%10)
    else:
        if carry:
            head = insert_begin(head, carry)

    return head
    


"""
TEST CASES
"""

"""
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
node1 = ListNode(7)
node1.next = ListNode(2)
node1.next.next = ListNode(4)
node1.next.next.next = ListNode(3)

node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)


# node1 = ListNode(0)
# node2 = ListNode(0)

# node1 = ListNode(5)
# node2 = ListNode(5)


print(print_list(node1))
print(print_list(node2))
#print(print_list(add_two_numbers2(node1, node2)))
print(print_list(addTwoNumbers(node1, node2)))

# new_node = add_two_numbers(node1, node2)
# print(print_list(new_node))

