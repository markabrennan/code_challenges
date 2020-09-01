"""
Another attempt at deleting a BST
node, per Leet code problem.
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

def prev_node(root):
    if root is not None and root.left is not None:
        root = root.left
    while root.right:
        root = root.right
    return root.val

def next_node(root):
    if root is not None and root.right is not None:
        root = root.right
    while root.left:
        root = root.left
    return root.val

def del_node(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = del_node(root.left, val)
    elif val > root.val:
        root.right = del_node(root.right, val)
    elif val == root.val:
        if root.left is None and root.right is None:
            root = None
        elif root.right is not None:
            root.val = next_node(root)
            root.right = del_node(root.right, root.val)
        elif root.left is not None:
            root.val = prev_node(root)
            root.left =  del_node(root.left, val)

    return root
       
def insert_node(root, val):
    if root is None:
        root = TreeNode(val)
        return root
    if val < root.val:
        root.left = insert_node(root.left, val)
    elif val > root.val:
        root.right = insert_node(root.right, val)

    return root

    


"""
TEST CASES
"""

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)

print(inorder(root))
print(preorder(root))
print(postorder(root))

print(prev_node(root))
print(next_node(root))

#new_root = del_node(root, 3)

new_root = insert_node(root, 1)

print(inorder(new_root))
print(preorder(root))