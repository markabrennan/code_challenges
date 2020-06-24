"""
Leet Code 938: Range Sum of BST
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(root):
    vals = []
    def _pre(root):
        # root -> left -> right
        nonlocal vals
        if root is None:
            return
        vals.append(root.val)
        _pre(root.left)
        _pre(root.right)
    _pre(root)
    return vals

def inorder(root):
    vals = []
    def _in(root):
        nonlocal vals
        if root is None:
            return
        _in(root.left)
        vals.append(root.val)
        _in(root.right)
    _in(root)
    return vals

def postorder(root):
    vals = []
    def _post(root):
        nonlocal vals
        if root is None:
            return
        _post(root.left)
        _post(root.right)
        vals.append(root.val)
    _post(root)
    return vals


def range_sum_bst(root, L, R):
    sum_val = 0
    def _recurse(root, L, R):
        nonlocal sum_val
        if root is None:
            return
        _recurse(root.left, L, R)
        if L <= root.val <= R:
            sum_val += root.val
        _recurse(root.right, L, R)
    _recurse(root, L, R)
    return sum_val


"""
TEST CASES
"""

"""
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
"""

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)
# root.right.right = TreeNode(18)


"""
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)

root.left.left.left = TreeNode(1)
root.left.right.left = TreeNode(6)

# print(preorder(root))
# print(inorder(root))
# print(postorder(root))

print(range_sum_bst(root,6, 10))