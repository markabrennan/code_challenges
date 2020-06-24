"""
Extra practice with linked lists
"""

class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class List:
    def __init__(self, nums):
        self.head = None
        self.tail = None
        self.mappings = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in self.mappings:
                cur_count, node = self.mappings[val]
                cur_count += 1
                if node:
                    self.del_node(node)
                self.mappings[val] = (cur_count, None)
            else:
                node = self.add_node(val)
                self.mappings[val] = (1, node)

    def add_node(self, val):    
        new_node = ListNode(val)
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

    def del_node(self, val):
        node = self.mappings[val][1]
        if node:
            # Base Case 
            if self.head is None or node is None: 
                return 
            # If node to be deleted is head node 
            if self.head == node: 
                self.head = node.next
            # Change next only if node to be deleted is NOT 
            # the last node 
            if node.next is not None: 
                node.next.prev = node.prev 
            # Change prev only if node to be deleted is NOT  
            # the first node 
            if node.prev is not None: 
                node.prev.next = node.next


    def get_vals(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
        
    def add_front(self, val):
        new_node = ListNode(val=val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_back(self, val):
        new_node = ListNode(val=val)
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail = new_node




def get_list_vals(node):
    vals = []
    cur = node
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals



"""
TEST CASES
"""

# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)

# a.next = b
# b.prev = a
# b.next = c
# c.prev = b

# print(get_list_vals(a))

ll = List([1,2,3])
print(ll.get_vals())
ll.add_node(5)
print(ll.get_vals())
ll.del_node(3)
print(ll.get_vals())

        


