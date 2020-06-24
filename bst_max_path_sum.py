"""
Leet Code April Daily Challenge:
Binary Tree Maximum Path Sum
"""


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_level_order(vals):
    Q = deque()
    root = TreeNode(vals[0])
    Q.append(root)
    ix = 1
    while Q and ix < len(vals):
        node = Q.popleft()
        val = vals[ix]
        if val is not None:
            node.left = TreeNode(val)
            Q.append(node.left)
        ix += 1
        if ix < len(vals) and vals[ix] is not None:
            val = vals[ix]
            node.right = TreeNode(val)
            Q.append(node.right)
        ix += 1
    
    return root

def inorder(root):
    vals = []
    def recurse(root):
        nonlocal vals
        if root is None:
            return
        # go left
        recurse(root.left)
        # root
        if root.val is not None:
            vals.append(root.val)
        # go right
        recurse(root.right)
    recurse(root)
    return vals

def postorder(root):
    vals = []
    def recurse(root):
        nonlocal vals
        if root is None:
            return
        recurse(root.left)
        recurse(root.right)
        if root.val is not None:
            vals.append(root.val)
    recurse(root)
    return vals

def preorder(root):
    vals = []
    def recurse(root):
        nonlocal vals
        if root is None:
            return
        if root.val is not None:
            vals.append(root.val)
        recurse(root.left)
        recurse(root.right)
    recurse(root)
    return vals

def levelorder(root):
    vals = []
    Q = deque()
    vals.append(root.val)
    Q.append(root)
    while Q:
        node = Q.popleft()
        if node.left:
            if node.left.val is not None:
                vals.append(node.left.val)
            Q.append(node.left)
        if node.right:
            if node.right.val is not None:
                vals.append(node.right.val)
            Q.append(node.right)
    return vals

import math
def max_path_sum(root):
    running = 0
    max_sum = -1 * math.inf
    def recurse(root, cur_val):
        nonlocal running
        nonlocal max_sum
        if root is None:
            return
        
        running = max(running, root.val, running+root.val)

        max_sum = max(max_sum, root.val, running)

        recurse(root.left, cur_val)
        running = max(running, root.val)
        recurse(root.right, cur_val)

    recurse(root,0)
    return max_sum

"""
TEST CASES
"""

# vals = [1,2,3]  # expected result:  6
# tree = make_tree_level_order(vals)

vals =  [-10,9,20,None,None,15,7]  # expected result:  42
tree = make_tree_level_order(vals)

# vals = [1,-2,-3,1,3,-2,None,-1]  # expected:  3
# tree = make_tree_level_order(vals)

# vals = [1,-2,3]  # expected:  4
# tree = make_tree_level_order(vals)

# vals = [1,2,None,3,None,4,None,5]  # expected:  15
# tree = make_tree_level_order(vals)

print(inorder(tree))
print(postorder(tree))
print(preorder(tree))
print(levelorder(tree))
print(max_path_sum(tree))