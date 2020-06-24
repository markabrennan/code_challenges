"""
Leet Code 226. Invert Binary Tree
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Pre-Order
"""
def preorder(root):
    results = []
    def _preorder(root):
        nonlocal results
        if root is None:
            return
        results.append(root.val)
        _preorder(root.left)
        _preorder(root.right)
    
    _preorder(root)
    return results

"""
Post-Order
"""
def postorder(root):
    results = []
    def _postorder(root):
        nonlocal results
        if root is None:
            return
        _postorder(root.left)
        _postorder(root.right)
        results.append(root.val)

    _postorder(root)
    return results


"""
Inorder
"""
def inorder(root):
    results = []
    def _inorder(root):
        nonlocal results
        if root is None:
            return
        _inorder(root.left)
        results.append(root.val)
        _inorder(root.right)
    _inorder(root)
    return results


def invert_binary_tree(root):
    if root is None:
        return None
    left = invert_binary_tree(root.left)
    right = invert_binary_tree(root.right)
    root.left = right
    root.right = left
    return root


"""
TEST CASE
"""
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(inorder(root))
new_root = invert_binary_tree(root)
print(inorder(new_root))
