"""Leet Code Problem
find closest value in a BST
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def closest_val(root, target):
    vals_dist = []
    def dfs(root, target):
        nonlocal vals_dist
        if root is None:
            return
        vals_dist.append((abs(root.val - round(target,0)), root.val))
        dfs(root.left, target)
        dfs(root.right, target)

    dfs(root, target)
    return sorted(vals_dist)[0][1]
       



"""
TEST CASES
"""
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)

print(inorder(root))
print(preorder(root))
print(postorder(root))
print(closest_val(root, 3.714286))