from collections import deque


class Node:
    def __init__(self, data=None, left=None, Right=None):
        self.data = data
        self.left = left
        self.right = Right



def level_order(root):
    vals = []
    Q = deque()
    Q.append(root)

    while Q:
        node = Q.popleft()
        if node:
            vals.append(node.data)
        if node.left:
           Q.append(node.left)
        if node.right:
            Q.append(node.right)

    return vals


def inorder(root):
    vals = []

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        vals.append(root.data)
        dfs(root.right)

    dfs(root)
    return vals


def preorder(root):
    vals = []

    def dfs(root):
        if not root:
            return
        vals.append(root.data)    
        dfs(root.left) 
        dfs(root.right)

    dfs(root)
    return vals


def postorder(root):
    vals = []

    def dfs(root):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        vals.append(root.data) 

    dfs(root)
    return vals



"""
TEST CASES
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print(level_order(root))
print(inorder(root))
print(preorder(root))
print(postorder(root))

