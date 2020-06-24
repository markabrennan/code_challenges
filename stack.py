class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        if self.min is None:
            self.stack.append(x)
            self.min = x
        else:
            if x < self.min:
                self.min = x
                self.stack.append(x)
            else:
                self.stack.append(x)

    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.min:
            if len(self.stack) >= 1:
                self.min = min(self.stack)
            else:
                self.min = None
        return item

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

    def __str__(self):
        return self.stack.__str__()



    def old_getMin(self) -> int:
        return self.top()

    def old_top(self) -> int:
        top = self.head.data
        return top

    def old_pop(self) -> None:
        self.head = self.head.next

    def old_push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(data=x)
        else:
            top = self.head.data
            if x < top:
                new_node = Node(data=x)
                new_node.next = self.head
                self.head = new_node
            else:
                new_node = Node(data=x)
                self.head.next = new_node

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

