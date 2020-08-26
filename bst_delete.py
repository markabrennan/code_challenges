"""
Another attempt (by memory) of the 
Leet Code problem of deleting a node
from a BST
"""

from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return []
    else:
        return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if root is None:
        return []
    else:
        return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if root is None:
        return []
    else:
        return postorder(root.left) + postorder(root.right) + [root.val]

def levelorder(root):
    vals = []
    Q = deque()
    Q.append(root)
    while Q:
        node = Q.popleft()
        if node is not None:
            vals.append(node.val)
        if node.left is not None:
            Q.append(node.left)
        if node.right is not None:
            Q.append(node.right)
    return vals

def successor(root):
    if root is None:
        return root
    root = root.right
    while root.left:
        root = root.left
    return root.val

def predecessor(root):
    if root is None:
        return root
    root = root.left
    while root.right:
        root = root.right
    return root.val

def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root = delete_node(root.left, key)
    elif key > root.val:
        root = delete_node(root.right, key)
    else:
        if root.left is None and root.right is None:
            root = None
            return root
        elif root.right:
            root.val = successor(root)
            root = delete_node(root.right, root.val)
        else:
            root.val = predecessor(root)
            root = delete_node(root.left, root.val)
    return root

def insert_node(root, val):
    if root is None:
        return TreeNode(val=val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    elif val > root.val:
        root.right = insert_node(root.right, val)
    return root

def search_bst(root, val):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    else:
        return search_bst(root.right, val)



    


"""
TEST CASES
"""

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(5)


print(inorder(root))
print(preorder(root))
print(postorder(root))
print(levelorder(root))

print(successor(root))
print(predecessor(root))