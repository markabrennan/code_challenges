"""
Circular Array Problem from
Grokking the Coding Interview
https://www.educative.io/courses/grokking-the-coding-interview/3jY0GKpPDxr
"""


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_list(head):
    vals = []
    cur = head
    while cur:
        if  cur.value in vals:
            break
        vals.append(cur.value)
        cur = cur.next
    return vals


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
    return p1


def make_list(arr):
    node_list = []
    for i, v in enumerate(arr):
        next_pos = i + v
        if next_pos >= len(arr):
            next_pos = abs(len(arr) - next_pos)
        node = Node(value=next_pos)
        node_list.append(node)
        
    for ix, node in enumerate(node_list):
        next_val = node.value            
        node.next = node_list[next_val]
        node.value = ix

    return node_list[0]

def circular_array_loop_exists(arr):
    ln = len(arr)
    for i, v in enumerate(arr):
        next_pos = i + v
        print(f'next_pos = {next_pos}')
        if i + v >= ln or i + v < 0:
            return True
    return False

"""
Official solution
"""
def circular_array_loop_exists2(arr):
  for i in range(len(arr)):
    is_forward = arr[i] >= 0  # if we are moving forward or not
    slow, fast = i, i

    # if slow or fast becomes '-1' this means we can't find cycle for this number
    while True:
      # move one step for slow pointer
      slow = find_next_index(arr, is_forward, slow)
      # move one step for fast pointer
      fast = find_next_index(arr, is_forward, fast)
      if (fast != -1):
        # move another step for fast pointer
        fast = find_next_index(arr, is_forward, fast)
      if slow == -1 or fast == -1 or slow == fast:
        break

    if slow != -1 and slow == fast:
      return True

  return False


def find_next_index(arr, is_forward, current_index):
  direction = arr[current_index] >= 0

  if is_forward != direction:
    return -1  # change in direction, return -1

  next_index = (current_index + arr[current_index]) % len(arr)

  # one element cycle, return -1
  if next_index == current_index:
    next_index = -1

  return next_index


"""
TEST CASES
"""

"""
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
"""
#arr = [1, 2, -1, 2, 2]

"""
Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1
"""

"""
Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.
"""
arr = [2, 1, -1, -2]

# list_head = make_list(arr)
# print(print_list(list_head))
# cycle_start_node = find_cycle_start(list_head)
# print(f'cycle length:  {count_cycle(list_head)}')

print(circular_array_loop_exists2(arr))