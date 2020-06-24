"""
Leet Code April Daily Coding Challenge
First Unique Number
Couple of different ways to implement:
1) Linked List with hash map
2) Queue
3) Heap

"""

class FirstUnique:
    class ListNode:
        def __init__(self, val=None, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, nums):
        self.mappings = {}
        self.head = None
        self.tail = None
        for i in nums:
            if i in self.mappings:
                cur_count, node = self.mappings[i]
                cur_count += 1
                if node:
                    self.del_node(node)
                self.mappings[i] = (cur_count, None)
            else:
                node = self.add_node(i)
                self.mappings[i] = (1, node)

    def add_front(self, val):
        new_node = FirstUnique.ListNode(val=val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.head.next = self.tail
            self.tail.prev = new_node

    def add_node(self, val):    
        new_node = FirstUnique.ListNode(val)
        if self.head is None:    
            #Both head and tail will point to newNode    
            self.head = self.tail = new_node
            #head's previous will point to None    
            self.head.prev = None
            #tail's next will point to None, as it is the last node of the list    
            self.tail.next = None
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = new_node
            #newNode's previous will point to tail    
            new_node.prev = self.tail
            #newNode will become new tail    
            self.tail = new_node
            #As it is last node, tail's next will point to None    
            self.tail.next = None
        return new_node

    def print_list(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
                
    def del_node(self, node):
        if node:
            if node.prev is None:
                if self.head.next:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head = None
            elif node.next is not None:
                node.prev = node.next
                node.next.prev = node.prev
            else:
                node.prev.next = None

    def showFirstUnique(self) -> int:
        if self.head and self.head.val:
            return self.head.val
        else:
            return -1
        
    def add(self, value: int) -> None:
        if value in self.mappings:
            cur_count, node = self.mappings[value]
            if node:
                self.del_node(node)
            cur_count += 1
            self.mappings[value] = (cur_count, None)
        else:
            node = self.add_node(value)
            self.mappings[value] = (1, node)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


"""
TEST CASES
"""

# f = FirstUnique([2,3,5])
# print(f.showFirstUnique())
# f.add(5)
# print(f.showFirstUnique())
# f.add(2)
# print(f.showFirstUnique())
# print(f.print_list())
# f.add(3)
# print(f.showFirstUnique())

# f = FirstUnique([7,7,7,7,7,7])
# print(f.showFirstUnique())
# f.add(7)
# f.add(3)
# f.add(3)
# f.add(7)
# f.add(17)
# print(f.showFirstUnique())

f = FirstUnique([809])
print(f.showFirstUnique())
f.add(809)
print(f.showFirstUnique())



# First test doubly-linked list and try to delete
# a node in the middle!

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)

# a.next = b
# b.prev = a
# b.next = c
# c.prev = b

# def del_node(node):
#     nxt = node.next
#     prev = None
#     if node.prev is None:
#         node = node.next
#         node.prev = None
#         return node
#     else:
#         prev = node.prev
#         prev.next = nxt
#         nxt.prev = prev
#         return prev

# def print_list(node):
#     vals = []
#     cur = node
#     while cur:
#         vals.append(cur.val)
#         cur = cur.next
#     return vals

# print(print_list(a))
# ret = del_node(a)
# print(print_list(ret))
# print(print_list(a))
