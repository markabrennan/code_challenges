"""
Leet Code April Daily Challenge:
Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
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


def is_valid_seq(root, arr):
    vals = []
    is_valid = False
    def recurse(root, vals, pos):
        nonlocal is_valid
        if root is None:
            if vals == arr:
                is_valid = True
            return root
        if root.val is not None:
            vals.append(root.val)
        recurse(root.left, vals)
        recurse(root.right, vals)

    recurse(root, vals, 0)
    return is_valid

    
def is_valid_seq2(root, arr):
    is_valid = False
    nums = []
    def recurse(node, nums, pos):
        nonlocal is_valid
        if node is None:
            # if pos <= len(arr) and nums == arr:
            #     is_valid = True
            return node
        if node.val is not None and pos < len(arr) and node.val == arr[pos]:
#            nums.append(node.val)
            recurse(node.left, nums, pos+1)
            recurse(node.right, nums, pos+1)
            #if pos < len(arr) and nums == arr and node.left is None and node.right is None and pos != 0:
            if pos == len(arr)-1 and node.left is None and node.right is None:
                is_valid = True

    recurse(root, nums, 0)
    return is_valid


def is_valid_seq3(root, arr):
    is_valid = False
    def recurse(node, pos):
        nonlocal is_valid
        if node is None:
            return node
        if node.val is not None and pos < len(arr) and node.val == arr[pos]:
            recurse(node.left, pos+1)
            recurse(node.right, pos+1)
            if pos == len(arr)-1 and node.left is None and node.right is None:
                is_valid = True

    recurse(root, 0)
    return is_valid

            

# vals = [0,1,0,0,1,0,None,None,1,0,0]
# root = make_tree_level_order(vals)
#print(inorder(root))


# tree = TreeNode(0)
# tree.left = TreeNode(1)
# tree.right = TreeNode(0)
# tree.left.left = TreeNode(0)
# tree.left.left.right = TreeNode(1)

# tree.left.right = TreeNode(1)

# tree.left.right.left = TreeNode(0)
# tree.left.right.right = TreeNode(0)

# tree.right.left = TreeNode(0)

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
# tree.right.left = TreeNode(6)

# tree.left.left.right = TreeNode(7)
# tree.left.right.left = TreeNode(8)
#tree.left.right.right = TreeNode(9)

#vals = [1,2,3,4,5,6,None,None,7,8,9]
#vals = [0,1,0,0,1,0,None,None,1,0,0]

vals = [4,None,2,7,5,3,4,4]
arr = [4,2,7,4]  # result:  True
tree = make_tree_level_order(vals)

# vals = [0,1,0,0,1,0,None,None,1,0,0]
# tree = make_tree_level_order(vals)
# arr = [0,1,0,1]  # result: True
##arr = [0,0,1]   # result:  False
#arr = [0,1,1]  # result:  False

# vals = [8,3,None,2,1,5,4]
# arr = [8]
# tree = make_tree_level_order(vals)

# vals = [0,1,0,0,1,0,None,None,1,0,0]
# arr = [0,1,0,1]   # result:  True
# tree = make_tree_level_order(vals)


# vals = [0,9,0,5,6,6,9,2,8,1,6,9,5,6,3,1,4,1,9,9,1,0,1,9,7,0,4,6,5,2,7,3,3,6,9,8,2,9,1,8,5,9,2,None,5,3,4,7,6,5,3,2,7,6,4,0,2,0,5,8,4,1,2,9,0,None,2,7,8,7,4,9,None,9,3,9,7,0,7,3,7,None,7,3,5,4,1,1,8,None,7,7,9,4,2,6,0,None,5,5,4,1,0,7,4,9,8,2,8,5,2,None,None,1,9,0,5,7,3,None,None,9,4,3,6,2,9,1,1,8,5,0,None,8,None,6,8,4,5,2,3,None,None,None,None,0,None,2,9,1,None,None,None,8,None,7,None,1,1,None,5,8,9,5,6,None,4,5,9,None,4,6,None,None,1,8,None,6,3,4,5,7,3,3,9,8,None,0,1,3,9,9,0,4,3,1,3,9,2,1,9,5,None,1,8,3,6,None,None,5,3,None,2,2,4,6,9,8,2,None,5,2,None,None,4,1,6,None,9,5,8,3,None,None,8,3,None,7,6,None,6,4,None,None,None,None,None,7,0,9,4,6,5,2,3,None,0,2,1,None,None,8,3,None,None,None,None,None,None,1,0,None,None,None,4,None,9,None,7,None,None,5,7,None,2,None,0,None,5,None,None,None,None,None,0,4,None,2,3,2,None,5,None,1,5,3,None,None,6,2,4,1,9,9,3,None,None,3,9,0,None,7,7,2,8,9,8,8,2,6,9,4,6,3,0,5,0,8,None,None,5,5,6,3,0,6,9,0,0,1,0,1,0,7,2,None,None,None,None,None,None,None,None,0,6,8,4,None,5,3,0,9,None,None,None,None,5,7,9,0,8,4,6,3,5,9,None,None,None,None,None,None,None,None,None,9,9,0,None,None,9,1,9,6,6,None,1,2,None,2,4,4,7,5,4,0,1,4,9,None,8,3,None,None,None,0,None,4,None,None,6,None,None,None,None,None,None,None,None,4,None,None,None,None,None,None,None,None,None,0,None,None,None,None,None,None,None,2,8,None,None,8,6,1,6,None,4,1,2,0,None,None,0,2,None,2,7,7,0,6,4,1,4,1,9,9,7,0,8,7,7,3,5,7,1,8,None,2,8,9,None,5,4,0,5,4,None,3,6,5,7,0,4,None,5,7,8,8,2,None,None,None,None,3,4,None,1,8,6,4,7,7,7,6,None,8,8,None,1,0,9,None,None,5,8,4,7,None,7,None,3,2,None,None,None,None,4,0,3,3,5,8,2,None,7,4,9,None,None,None,0,4,8,3,0,7,0,4,None,3,None,None,None,6,8,6,None,1,2,2,6,None,None,None,None,3,7,None,0,7,1,5,3,None,None,9,6,None,None,None,7,7,2,6,3,None,None,9,7,0,9,0,None,4,5,1,3,2,None,None,None,7,None,None,None,None,None,None,None,None,9,None,None,5,9,None,9,None,None,9,6,None,2,None,None,None,None,None,None,6,None,7,9,2,6,4,3,None,0,None,None,1,3,1,4,3,4,7,None,None,None,None,None,0,None,7,6,3,4,None,3,3,9,None,None,8,8,6,4,0,None,4,0,None,4,None,6,3,6,7,None,None,None,0,2,6,0,8,2,None,9,4,1,5,9,9,1,0,0,4,6,1,1,3,None,6,0,3,7,1,3,7,4,9,0,None,4,9,None,None,9,4,0,2,6,4,None,None,None,0,None,3,3,4,6,None,None,4,None,None,None,5,None,None,3,0,3,None,None,9,1,0,None,6,8,2,None,None,None,None,5,None,None,5,None,8,None,None,None,6,None,4,None,5,None,0,None,None,7,3,None,None,None,9,None,None,1,9,4,None,4,2,None,None,None,3,7,None,None,None,5,7,None,None,None,8,None,None,None,None,None,None,None,5,None,None,None,None,2,3,6,None,None,1,None,3,3,None,None,None,None,None,2,4,0,None,7,None,2,4,1,2,6,None,0,None,8,None,8,8,0,None,8,0,None,0,None,None,9,None,None,None,None,4,2,4,8,None,None,None,None,None,7,None,None,None,None,None,5,1,None,None,None,8,None,9,4,None,None,1,None,7,5,8,9,0,None,None,None,None,None,1,2,7,None,None,1,2,7,4,8,6,6,4,0,9,3,None,None,2,None,None,None,None,None,None,None,None,None,8,None,0,None,5,3,4,None,4,7,5,None,None,None,None,9,6,0,7,4,7,4,7,0,None,0,9,1,3,None,9,None,None,None,6,1,None,None,2,9,9,5,2,9,None,None,5,8,5,4,8,1,9,6,9,9,7,8,5,None,0,4,9,2,1,7,3,8,7,9,None,0,3,9,7,9,8,None,3,5,None,None,0,6,None,None,2,6,None,9,None,None,0,None,None,None,None,None,None,None,2,None,None,None,None,1,None,4,None,None,2,6,0,2,0,2,None,None,None,None,None,0,2,9,5,4,None,None,None,None,1,8,None,4,None,None,None,7,None,4,None,None,None,5,None,9,None,None,6,None,9,6,None,3,None,None,None,None,3,None,None,None,9,1,None,None,7,None,None,6,8,None,None,None,None,None,None,None,4,None,None,None,9,None,None,None,None,None,9,8,None,0,7,1,2,0,None,None,None,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,2,1,None,None,5,None,None,None,5,None,None,6,None,None,None,None,None,1,None,None,9,None,3,6,None,None,1,9,3,1,2,7,8,None,None,None,1,None,None,None,None,None,8,9,0,None,9,None,1,None,None,None,5,1,7,None,3,0,None,None,None,0,None,None,None,None,3,4,None,None,2,None,0,None,6,None,None,None,None,None,9,None,2,3,4,4,0,9,7,4,6,None,None,None,5,0,None,6,None,None,None,5,2,7,None,5,None,8,None,6,0,4,None,None,6,1,0,6,6,None,2,None,None,7,5,2,7,None,0,2,7,None,3,3,3,None,6,3,2,4,None,1,9,None,2,None,1,8,None,7,4,0,0,2,3,3,None,None,None,None,None,None,5,2,7,4,4,7,7,None,8,7,None,None,None,None,None,None,7,8,None,None,None,None,None,7,1,0,None,1,None,8,None,None,None,None,None,None,None,2,1,5,None,None,None,None,2,6,None,None,8,5,4,4,0,1,None,7,8,None,None,None,None,0,None,4,5,0,2,None,3,9,None,None,None,4,9,None,9,None,None,None,7,7,None,0,None,None,None,5,None,6,0,0,None,None,None,None,None,None,None,None,None,9,None,None,0,None,3,7,None,6,None,None,None,None,None,None,None,1,9,6,None,7,1,2,7,3,7,4,None,None,None,None,None,None,3,1,1,9,2,6,None,None,None,3,9,0,3,1,None,None,None,None,4,None,None,0,None,None,None,1,9,0,None,0,2,8,6,None,None,None,None,None,1,None,6,4,None,None,None,None,None,None,None,None,6,None,None,1,None,None,None,None,6,4,6,7,None,None,4,5,None,None,None,4,None,4,None,3,None,1,8,5,None,4,None,None,None,6,4,1,1,0,0,0,6,4,None,3,4,6,9,None,2,None,None,4,None,None,8,None,None,None,None,None,None,None,None,None,0,8,None,6,None,None,2,0,8,None,9,7,None,None,3,7,None,None,8,None,None,0,2,None,1,None,6,4,5,0,0,9,7,4,None,9,5,7,3,4,None,None,None,4,7,3,None,5,4,None,9,None,None,6,7,None,None,None,None,None,None,None,5,2,None,None,None,None,7,None,None,None,3,8,7,None,None,None,None,None,0,3,None,None,7,5,None,None,2,8,None,None,None,0,None,None,None,None,None,None,None,None,None,4,None,None,6,3,None,None,None,None,None,None,None,None,9,0,8,None,6,1,None,None,None,9,None,None,None,4,3,None,None,None,5,None,8,3,2,9,5,7,None,3,6,None,1,None,3,3,None,None,8,None,None,None,None,None,None,None,2,1,3,6,None,None,7,None,2,None,None,None,None,None,None,4,9,None,3,None,5,None,None,5,None,None,None,None,None,None,None,None,None,4,None,None,1,None,2,None,None,None,None,None,None,None,None,None,None,2,0,0,None,None,None,None,4,3,4,1,8,7,6,1,3,None,None,8,None,None,None,None,None,None,None,None,None,7,None,None,5,9,None,None,None,0,9,5,4,1,9,None,0,3,8,5,None,9,6,0,None,2,9,8,1,None,None,None,2,None,0,2,None,8,None,None,None,6,7,0,0,6,4,None,2,0,None,None,None,9,None,2,5,3,None,None,None,None,None,9,5,None,6,1,None,0,3,6,8,1,6,1,None,6,9,2,0,8,8,5,1,8,2,8,0,None,None,None,None,7,None,None,None,None,None,None,None,None,None,4,None,4,None,8,7,None,None,None,None,None,8,6,None,5,2,None,None,None,None,None,8,None,None,6,None,8,None,None,None,None,None,None,5,None,None,None,9,7,0,0,None,None,None,None,None,8,None,1,None,None,None,None,None,None,None,None,2,None,7,7,None,7,4,None,None,None,None,None,None,None,8,None,None,None,1,None,0,2,None,None,None,None,None,3,None,3,6,9,5,None,0,None,1,None,None,6,None,4,None,None,None,None,None,5,None,None,6,None,7,0,6,8,3,None,5,None,7,7,None,None,2,None,5,None,None,9,None,6,None,None,None,1,None,None,None,None,None,None,None,None,None,None,5,None,None,None,None,2,6,6,None,9,None,4,None,2,9,3,None,None,3,7,2,1,5,6,None,None,None,None,0,None,6,7,2,0,5,None,None,None,None,6,None,6,7,None,None,None,4,None,None,4,None,5,None,None,None,None,None,None,None,None,8,5,None,None,None,0,7,8,None,0,1,6,9,7,5,0,None,9,7,1,None,None,None,None,None,None,None,None,8,2,None,6,None,3,1,3,1,4,6,3,5,5,4,5,None,None,None,None,7,3,None,None,None,3,None,6,None,None,5,None,4,9,4,None,3,None,None,None,None,None,None,None,None,None,None,None,9,None,None,None,None,None,None,6,None,None,None,None,3,6,None,None,None,None,None,None,3,None,None,None,None,None,4,None,None,None,None,None,None,6,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,8,None,9,5,None,9,6,0,7,3,9,None,None,3,9,None,None,4,None,None,None,None,None,None,None,None,1,8,None,None,None,None,7,None,6,7,5,None,None,6,5,None,None,None,None,None,None,None,None,None,0,1,None,None,None,8,0,0,3,None,None,None,None,None,0,0,None,None,None,6,3,None,4,5,3,None,None,None,9,None,None,None,None,None,7,5,4,8,6,5,1,None,4,5,3,None,8,1,2,7,6,8,9,6,None,None,None,None,None,6,None,3,7,None,None,6,0,None,None,None,None,6,4,9,2,9,3,1,None,5,7,None,None,None,None,1,1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0,None,None,None,2,None,None,6,None,None,None,None,None,None,7,None,None,None,None,0,8,None,None,3,None,None,None,None,None,None,None,None,None,3,None,None,None,None,None,None,None,None,5,None,None,None,None,9,None,5,None,4,None,None,None,None,None,None,None,2,None,None,None,7,None,None,1,5,7,8,None,None,8,None,None,1,None,3,None,None,4,6,None,None,9,None,None,None,1,2,4,None,1,1,None,None,3,None,4,3,None,None,None,5,6,0,6,4,3,8,None,9,None,None,None,9,None,None,None,0,7,None,None,3,None,9,8,1,2,7,7,None,None,4,None,6,8,3,9,None,None,2,None,None,8,None,None,None,8,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,None,None,7,None,None,None,None,None,None,None,None,None,5,None,None,None,None,0,None,None,None,None,None,None,None,None,None,None,None,4,None,3,None,8,2,0,None,None,None,None,0,None,None,6,None,None,None,7,None,None,8,3,0,None,None,None,None,None,None,4,4,None,None,None,None,1,None,None,3,None,None,2,None,5,8,None,None,None,None,None,None,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,None,None,2,None,None,None,None,None,None,None,None,None,None,3,8,3,5,None,None,None,4,None,None,8,None,0,0,None,2,None,1,None,7,None,5,9,2,None,None,None,9,3,0,3,None,None,None,None,6,0,6,None,5,8,None,7,7,None,None,None,None,None,2,4,9,None,None,None,None,None,5,None,6,None,None,None,None,None,None,5,None,None,None,None,None,None,8,None,9]
# tree = make_tree_level_order(vals)
# arr = [0,0,6,9,9,7,4,6,2,8,9,4,5,7,3,8]   # result:  True



print(inorder(tree))
print(postorder(tree))
print(preorder(tree))
print(levelorder(tree))
print(is_valid_seq3(tree, arr))

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
# print(inorder(tree))
#print(is_valid_seq(tree, arr))

# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
# print(inorder(tree))
# print(postorder(tree))
# print(preorder(tree))
# print(levelorder(tree))