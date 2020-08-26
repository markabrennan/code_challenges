"""
Leet Code Vertical Order Traversal of a Binary Tree
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3415/
"""

from collections import deque
from collections import OrderedDict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_levels(root):
    levels = []
    Q = deque()
    d = {}
    X = Y = 0
    Q.append((root, X, Y))

    while Q:
        node, cur_x, cur_y = Q.popleft()
        if node:
            if cur_x in d:
                d[cur_x].append((abs(cur_y),node.val))
            else:
                d[cur_x] = [(abs(cur_y), node.val)]
        if node.left:
            Q.append((node.left, cur_x-1, cur_y-1))
        if node.right:
            Q.append((node.right, cur_x+1, cur_y-1))
    print(d)
    for k in sorted(d.keys()):
        levels.append([x[1] for x in sorted(d[k])])
    return levels
        

def get_levels_with_list(root):
    """Same function as above - same approach - 
    but use a list with tuples (Y, X, val) instead
    of a dict keyed on Y.
    """
    levels = []
    Q = deque()
    d = []
    X = Y = 0
    Q.append((root, X, Y))

    while Q:
        node, cur_x, cur_y = Q.popleft()
        if node:
            levels.append((cur_x, abs(cur_y), node.val))
        if node.left:
            Q.append((node.left, cur_x-1, cur_y-1))
        if node.right:
            Q.append((node.right, cur_x+1, cur_y-1))
    print(levels)
    return sorted(levels)
        

def inorder_stack(root):
    if root is None:
        return []
    vals = []
    stack = []

    stack.append(root)
    while stack:
        node = stack.pop()
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
        if node.left is None and node.right is None:
            vals.append(node.val)
    return vals




"""
TEST CASES
"""

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# print(get_levels(root))


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)


# root = TreeNode(0)
# root.left = TreeNode(5)
# root.left.left = TreeNode(9)
# root.right = TreeNode(1)
# root.right.left = TreeNode(2)
# root.right.left.right = TreeNode(3)
# root.right.left.right.left = TreeNode(4)
# root.right.left.right.left.left = TreeNode(6)
# root.right.left.right.left.left.left = TreeNode(7)
# root.right.left.right.right = TreeNode(8)

# levels = get_levels_with_list(root)
# print(levels)

root = TreeNode(4)
root.left = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

root.right = TreeNode(7)
root.right.left = TreeNode(5)

print(inorder_stack(root))