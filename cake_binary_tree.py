"""
Interview Cake Binary Tree Problem
check for a balanced tree by calculating height;
height difference between any two leaf nodes is not
greater than 1 
"""

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_balanced(tree_root):
    depth = 0
    isbal = True

    # Determine if the tree is superbalanced
    def walk(tree_root):
        nonlocal isbal
        if tree_root is None:
            return 0
        lh = walk(tree_root.left)
        rh = walk(tree_root.right)

        print(f'before eval: node: {tree_root.value} | rh: {rh} | lh: {lh}')
        if lh > rh + 1 or rh > lh + 1:
            isbal = False

        print(f'end of walk: lh: {lh} | rh: {rh})')

        return max(lh, rh) + 1
        
    walk(tree_root)
    return isbal


def is_binary_search_tree(tree_root):
    # A tree with no nodes is superbalanced, since there are no leaves!
    if tree_root is None:
        return True

    nodes = []
    nodes.append(tree_root)

    root_val = tree_root.value
    while len(nodes):
        # Pop a node and its depth from the top of our stack
        node = nodes.pop()
        print(f'top of while: node: {node.value}')

        if node.left:
            print(f'node.value: {node.value} | node.left.value: {node.left.value}')
            if node.left.value > node.value or node.left.value < root_val:
                return False
            nodes.append(node.left)
        if node.right:
            print(f'node.value: {node.value} | node.right.value: {node.right.value}')
            if node.right.value < node.value or node.right.value < root_val:
                return False
            nodes.append(node.right)

    return True        


def is_balanced_iter(tree_root):
    # A tree with no nodes is superbalanced, since there are no leaves!
    if tree_root is None:
        return True

    # We short-circuit as soon as we find more than 2
    depths = []

    # We'll treat this list as a stack that will store tuples of (node, depth)
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        # Pop a node and its depth from the top of our stack
        node, depth = nodes.pop()
        print(f'top of while: node: {node.value} | depth: {depth}')

        # Case: we found a leaf
        if (not node.left) and (not node.right):
            # We only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                if ((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False
        else:
            # Case: this isn't a leaf - keep stepping down
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True        
    


def find_second_largest(root_node):
    def find_largest(root_node):

        if root_node.right:
            return find_largest(root_node.right)
        #return root_node.value
        return root_node

    max_node = find_largest(root_node)

    if max_node.left is not None:
        second_max_node = find_largest(max_node.left)


# tree = BinaryTreeNode(5)
# left = tree.insert_left(8)
# right = tree.insert_right(6)
# left.insert_left(1)
# left.insert_right(2)
# right.insert_left(3)
# right.insert_right(4)

# tree = BinaryTreeNode(1)
# left = tree.insert_left(5)
# right = tree.insert_right(9)
# right.left = right.insert_left(8)
# right.insert_right(5)
# right.left.insert_left(7) 


# tree = BinaryTreeNode(1)
# right = tree.insert_right(2)
# right_right = right.insert_right(3)
# right_right.insert_right(4)

# tree = BinaryTreeNode(1)
# left = tree.insert_left(2)
# right = tree.insert_right(4)
# left.insert_left(3)
# left.right = left.insert_right(7)
# left.right.insert_right(8)
# right.right = right.insert_right(5)
# right.right.right = right.right.insert_right(6)
# right.right.right.insert_right(9)


# result = is_balanced_iter(tree)
# print(result)


tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(70)
left.insert_left(10)
left.insert_right(40)
right.insert_left(60)
right.insert_right(80)

tree = BinaryTreeNode(50)
left = tree.insert_left(30)
right = tree.insert_right(80)
left.insert_left(20)
left.insert_right(60)
right.insert_left(70)
right.insert_right(90)

result = is_binary_search_tree(tree)
print(result)
