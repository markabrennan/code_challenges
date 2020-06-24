"""
Leet Code Problem 103:  Binary Tree Zigzag Level Order Traversal
"""

"""
I already coded a level order traversal, so am pasting here
"""

from collections import deque
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelorder(root):
    # breadth-first traversal
    # try it iteratively
    # add level grouping to make list of lists
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

    
def levelorder2(root):
    # breadth-first traversal
    # try it iteratively
    # add level grouping to make list of lists
    vals = []
    list_vals = []
    level = 0
    level_map = defaultdict(list)
    Q = deque()
    if root:
        Q.append((level, root))
    while Q:
        level, node = Q.popleft()
        level_map[level].append(node.val)
        vals.append(node.val)
        if node.left:
            Q.append((level+1,node.left))
        if node.right:
            Q.append((level+1, node.right))

    for vals in level_map.values():
        list_vals.append(vals)
    return list_vals

    
def levelorder_zig_zag(root):
    # breadth-first traversal
    # with zig zag
    # add level grouping to make list of lists
    vals = []
    list_vals = []
    level = 0
    level_map = defaultdict(list)
    Q = deque()
    if root:
        Q.append((level, root))
    while Q:
        level, node = Q.popleft()
        # if level % 2 != 0:  # odd level zig
        #     # first append value, then verse
        #     level_map[level].append(node.val)
        #     level_map[level] = level_map[level][::-1]
        # else:
        #     level_map[level].append(node.val)
        level_map[level].append(node.val) 
        vals.append(node.val)
        if node.left:
            Q.append((level+1,node.left))
        if node.right:
            Q.append((level+1, node.right))

    for level, vals in level_map.items():
        if level % 2 != 0:
            # odd level, so zig by reversing the list
            list_vals.append(vals[::-1])
        else:
            list_vals.append(vals)
#    return list_vals, level_map
    return list_vals


"""
Official Leet Code solution using
two queues, and avoiding the need to 
pass over the map at the end.
"""

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    ret = []
    level_list = deque()
    if root is None:
        return []
    # start with the level 0 with a delimiter
    node_queue = deque([root, None])
    is_order_left = True

    while len(node_queue) > 0:
        curr_node = node_queue.popleft()

        if curr_node:
            if is_order_left:
                level_list.append(curr_node.val)
            else:
                level_list.appendleft(curr_node.val)

            if curr_node.left:
                node_queue.append(curr_node.left)
            if curr_node.right:
                node_queue.append(curr_node.right)
        else:
            # we finish one level
            ret.append(level_list)
            # add a delimiter to mark the level
            if len(node_queue) > 0:
                node_queue.append(None)

            # prepare for the next level
            level_list = deque()
            is_order_left = not is_order_left

    return ret



"""
TEST CASES
"""

"""
level order tree:  [3,9,20,null,null,15,7]
result:
[
  [3],
  [20,9],
  [15,7]
]
"""

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

"""
level order tree:  [0,2,4,1,null,3,-1,5,1,null,6,null,8]
results:
[[0],[4,2],[1,3,-1],[8,6,1,5]]
"""

# root = TreeNode(0)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(1)
# root.left.left.left = TreeNode(5)
# root.left.left.right = TreeNode(1)

# root.right.left = TreeNode(3)
# root.right.right = TreeNode(-1)
# root.right.left.right = TreeNode(6) 
# root.right.right.right = TreeNode(8)

print(zigzagLevelOrder(root))

#print(levelorder_zig_zag(root))