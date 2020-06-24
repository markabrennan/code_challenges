"""
Leet Code April Daily Challenge
Min Stack
I did this previously, but wanted
to re-code it and make it more
efficient.
"""


"""
Original Version
"""

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



"""
New Version
- This uses a secondary list for
minimum values so that if the min
value is popped, you don't have to re-calculate
min
"""

class MinStack2:
    def __init__(self):
        self.stack = []
        self.mins = []
        self.min = None
    def push(self, x):
        if self.min is not None and x <= self.min:
            self.mins.append(self.min)
            self.min = x
        elif self.min is None:
            self.min = x
        self.stack.append(x)
    def pop(self):
        if self.stack[-1] == self.min and len(self.mins) > 0:
            self.min = self.mins.pop()
        elif self.stack[-1] == self.min:
            self.min = None
        return self.stack.pop()

    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min
    def __repr__(self):
        return f'{self.stack}'


"""
TEST CASES
"""
# minStack =  MinStack2()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack)
# print(minStack.getMin())  #   --> Returns -3.
# print(minStack.pop())
# print(minStack.top())     #       --> Returns 0.
# print(minStack.getMin())  #   --> Returns -2.


"""
Bad case - debug
"""

"""
["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
[[],[2],[0],[3],[0],[],[],[],[],[],[],[]]

Expected output:
[null,null,null,null,null,0,null,0,null,0,null,2]
"""

minStack = MinStack2()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())


"""
Another bad test case:
"""
"""
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]k
"""

minStack = MinStack2()
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
print(minStack.top())
print(minStack.pop())
print(minStack.getMin())
