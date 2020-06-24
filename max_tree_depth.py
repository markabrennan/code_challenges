"""
Leet Code 104. Maximum Depth of Binary Tree
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_tree_depth(root):
    max_depth = 0
    def _recurse(root):
        nonlocal max_depth
        if root is None:
            return 0
        lh = _recurse(root.left)
        rh = _recurse(root.right)
        max_depth = max(max_depth, rh, lh)
        return max(lh, rh) + 1

    _recurse(root)
    return max_depth + 1

"""
Re-write using iteration and stack
"""
def max_tree_depth_stack(root):
    stack = []
    stack.append((root, 1))
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node is not None:
            max_depth = max(depth, max_depth)
            stack.append((node.left, depth+1))
            stack.append((node.right, depth+1))
    return max_depth
            


"""
TEST CASES
"""
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(max_tree_depth_stack(root))
