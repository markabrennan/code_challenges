"""
Some practice with stacks and queues;
initial code is implementations of
a queue and a stack using a linked list;
next is an Interview Cake implementation of
a stack class using a list, and code to implement
max stack.
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next = next

class Queue:
    def __init__(self, node=None):
        self.head = Node()
        self.head.next = node
        self.tail = node
    def enqueue(self, data):
        temp = Node(data=data)
        if self.tail == None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
    def dequeue(self):
        # remove first item
        ret = self.head.data
        self.head = self.head.next
        return ret
    def print_queue(self):
        vals = []
        n = self.head
        while n:
            vals.append(n.data)
            n = n.next
        return vals


class Stack_q:
    def __init__(self, node=None):
        self.head = node
    def push(self, data):
        temp = Node(data=data)
        temp.next = self.head
        self.head = temp
    def pop(self):
        ret = None
        if self.head is not None:
            ret = self.head.data
            self.head = self.head.next
        return ret
    def print_stack(self):
        vals = []
        n = self.head
        while n:
            vals.append(n.data)
            n = n.next
        return vals



class Stack():
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.old_max_items = []
        self.max_item = None

    def push(self, item):
        """Push a new item onto the stack"""
        if item > self.max_item:
            self.old_max_items.append(self.max_item)
            self.max_item = item
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        ret = self.items.pop()
        if ret == self.max_item:
            self.max_item = self.old_max_items.pop()
        return ret

    def get_max(self):
        return self.max_item

    def _remax(self):
        return sorted(self.items, reverse=True)[0]


    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    # Implement the push, pop, and get_max methods


    def __init__(self):
        self.items = []
        self.old_max_items = []
        self.max_item = 0

    def push(self, item):
        if item >= self.max_item:
            self.old_max_items.append(self.max_item)
            self.max_item = item
        self.items.append(item)        

    def pop(self):
        if not self.items:
            return None
        ret = self.items.pop()
        if ret == self.max_item:
            self.max_item = self.old_max_items.pop()
        return ret


    def get_max(self):
        return self.max_item


"""
Class to implement a queue with two stacks - for Interview Cake
""""

class Queue_stack:
    def __init__(self):
        




# test Max Stack

max_stack = MaxStack()

max_stack.push(5)

actual = max_stack.get_max()
# expected = 5
# self.assertEqual(actual, expected)

max_stack.push(4)
max_stack.push(7)
max_stack.push(7)
max_stack.push(8)

print(f'stack items: {max_stack.items}')
print(f'old max values: {max_stack.old_max_items}')

actual = max_stack.get_max()
# expected = 8
#self.assertEqual(actual, expected)

actual = max_stack.pop()
print(f'just popped: {actual}')
print(f'max is: {max_stack.get_max()}')
print(f'stack items: {max_stack.items}')
print(f'old max values: {max_stack.old_max_items}')
# expected = 8
# self.assertEqual(actual, expected)

actual = max_stack.get_max()
# expected = 7
# self.assertEqual(actual, expected)

actual = max_stack.pop()
print(f'just popped: {actual}')
print(f'max is: {max_stack.get_max()}')
print(f'stack items: {max_stack.items}')
print(f'old max values: {max_stack.old_max_items}')
# expected = 7
# self.assertEqual(actual, expected)

actual = max_stack.get_max()
# expected = 7
# self.assertEqual(actual, expected)

actual = max_stack.pop()
print(f'just popped: {actual}')
print(f'max is: {max_stack.get_max()}')
print(f'stack items: {max_stack.items}')
print(f'old max values: {max_stack.old_max_items}')
# expected = 7        