"""
Leet Code Problem 987: Vertical Order Traversal of a Binary Tree
- Medium
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder(root):
    # left, root, right
    vals = []
    def recurse(root):
        nonlocal vals
        if root is None:
            return
        recurse(root.left)
        vals.append(root.val)
        recurse(root.right)
    recurse(root)
    return vals


def preorder(root):
    # root, left, right    
    vals = []
    def recurse(root):
        nonlocal vals
        if root is None:
            return
        vals.append(root.val)
        recurse(root.left)
        recurse(root.right)
    recurse(root)
    return vals

def postorder(root):
    # left, right, root
    vals = []
    def recurse(root):
        nonlocal vals
        if root is None:
            return
        recurse(root.left)
        recurse(root.right)
        vals.append(root.val)
    recurse(root)
    return vals

# def levelorder(root):
#     # breadth-first traversal
#     vals = []
#     def recurse(root):
#         nonlocal vals
#         if root is None:
#             return
#         vals.append(root.val)
#         if root.left:
#             vals.append(root.left.val)
#         if root.right:
#             vals.append(root.right.val)
#         recurse(root.left.left)
#         recurse(root.right.right)
#     recurse(root)
#     return vals

from collections import deque
def levelorder(root):
    # breadth-first traversal
    # try it iteratively
    vals = []
    Q = deque()
    if root:
        Q.append(root)
    while Q:
        node = Q.popleft()
        vals.append(node.val)
        if node.left:
            Q.append(node.left)
        if node.right:
            Q.append(node.right)
    return vals

def create_tree(vals):
    vals_q = deque(vals)
    tree_q = deque()
    root_val = vals_q.popleft()
    root = TreeNode(root_val)
    head = root
    tree_q.append(root)
    
    while vals_q and tree_q:
        node = tree_q.popleft()
        if node:
            lval = vals_q.popleft()
            if vals_q:
                rval = vals_q.popleft()
            if lval:
                node.left = TreeNode(lval)
            if rval:
                node.right = TreeNode(rval)
            tree_q.append(node.left)
            tree_q.append(node.right)
    return head



"""
solution attempt
"""
def vertical_traversal(root):
    vals = []
    def recurse(root, coordinates):
        nonlocal vals
        if root is None:
            return
        recurse(root.left, (coordinates[0]+(-1), coordinates[1]+(-1)))
        vals.append((root.val, coordinates[0], coordinates[1]))
        recurse(root.right, (coordinates[0]+1, coordinates[1]+(-1)))

    recurse(root, (0,0))
    #  [(4, -2, -2), (2, -1, -1), (5, 0, -2)...]
    print(f'values and coordinates:  {vals}')
    result_dict = {}
    for item in vals:
        level = item[1]
        if level not in result_dict:
            val = (item[2], item[0])
            result_dict[level] = [val]
            print(f'val: {val}')
        else:
            # get the val(s)
            val_list = result_dict[level]
            # add new val
            val_list.append((item[2], item[0]))
            val_list.sort(key=lambda x: abs(x[0]))
            val_list.sort(key=lambda x: x[1])
            result_dict[level] = val_list
            print(f'val list: {val_list}')
    
    res_list = []
    for val in result_dict.values():
        if len(val) > 1:
            sub = []
            for v in val:
                sub.append(v[1])
            res_list.append(sub)
        else:
            res_list.append([val[0][1]])

    return res_list

    # res_list =  [i[0] for i in result_dict.values()]
    # print(f'res_list:  {res_list}')
    # return res_list
        
       


"""
TEST CASES
"""

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right = TreeNode(3)

# print(inorder(root))
# print(preorder(root))
# print(postorder(root))
# print(levelorder(root))

"""
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).o
"""

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# vals = [3,9,20,None,None,15,7]
# new_tree = create_tree(vals)
# print(preorder(new_tree))
# print(vertical_traversal(new_tree))


# # root = TreeNode(1)
# # root.left = TreeNode(2)
# # root.left.left = TreeNode(4)
# # root.left.right = TreeNode(5)
# # root.right = TreeNode(3)
# # root.right.left = TreeNode(6)
# # root.right.right = TreeNode(7)

# # need to create this tree:
# [0,2,1,3,null,null,null,4,5,null,7,6,null,10,8,11,9]
# [0,2,1,3,None,None,None,4,5,None,7,6,None,10,8,11,9]
# root = TreeNode(0)
# root.left = TreeNode(2)
# root.right = TreeNode(1)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(5)
# root.left.left.left.right = TreeNode(7)
# root.left.left.right.eft = TreeNode(6)

# root.left.left.left.right.left = TreeNode(10)
# root.left.left.left.right.right = TreeNode(8)

# root.left.left.left.right.left.left = TreeNode(11)
# root.left.left.left.right.left.right = TreeNode(9)

# vals = [0,2,1,3,None,None,None,4,5,None,7,6,None,10,8,11,9]
# new_tree = create_tree(vals)
# print(vertical_traversal(new_tree))

vals = [0,10,1,None,None,2,4,3,5,None,None,6,None,7,9,8,None,None,None,None,11,None,None,12]
new_tree = create_tree(vals)
print(vertical_traversal(new_tree))




#print(inorder(root))

