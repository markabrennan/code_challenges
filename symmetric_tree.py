"""
Leet Code Problem # 101: "Symmetric Tree"
"""

# We need a tree node class
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


"""
Helper function to traverse tree - pre-order
"""
def preorder(node, vals):
    if node is None:
        return
    # root first
    vals.append(node.value)
    # go left
    preorder(node.left, vals)
    # go right
    preorder(node.right, vals)

    return vals

def inorder(node, vals):
    if node is None:
        return
    # go left
    inorder(node.left, vals)
    # get root
    vals.append(node.value)
    # go right
    inorder(node.right, vals)

    return vals

def postorder(node, vals):
    if node is None:
        return
    # go left
    postorder(node.left, vals)
    # go right
    postorder(node.right, vals)
    # get root
    vals.append(node.value)

    return vals


is_sym = True
def is_symmetric(node):
    global is_sym
    def recurse(l, r):
        global is_sym
        if l is None and r is not None:
            is_sym = False
            return
        if r is None and l is not None:
            is_sym  = False
            return
        if l is None and r is None:
            return
            
        if l.value != r.value:
            is_sym = False
            return

        recurse(l.left, r.right)
        recurse(l.right, r.left)

    recurse(node.left, node.right)
    return is_sym

class Solution:
    def is_symmetric(self, root):
        is_sym = True
        def recurse(l, r):
            nonlocal is_sym
            if l is None and r is not None:
                is_sym = False
                return
            if r is None and l is not None:
                is_sym  = False
                return
            if l is None and r is None:
                return
            if l.value != r.value:
                is_sym = False
                return
            recurse(l.left, r.right)
            recurse(l.right, r.left)

        recurse(root.left, root.right)
        return is_sym


"""
TEST CASES
"""
test1 = Node(val=1)
test1.left = Node(val=2)
test1.left.left = Node(val=3)
test1.left.right = Node(val=4)
test1.right = Node(val=2)
test1.right.left = Node(val=4)
test1.right.right = Node(val=3)

test2 = Node(val=1)
test2.left = Node(val=2)
test2.left.right = Node(val=3)
test2.right = Node(val=2)
test2.right.right = Node(val=3)


test_tree = Node(val=1)
test_tree.left = Node(val=2)
test_tree.left.left = Node(val=4)
test_tree.left.right = Node(val=5)
test_tree.right = Node(val=3)

# vals = []
# preorder(root, vals)
# print(vals)

# vals = []
# inorder(root, vals)
# print(vals)

# vals = []
# postorder(root, vals)
# print(vals)

#print(is_symmetric(test2))

print(Solution().is_symmetric(test2))

