"""
Leet Code April Daily Challenge
Diamter of a Binary Tree
(I've done this one before, but can't`
remember my solution...)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Previous code for this problem
which I don't want to review yet,
but am pasting here in order to 
save it.
"""
def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_max_left(root, num_edge=0):
            if root is None:
                return num_edge
            num_edge = get_max_left(root.left, num_edge+1)
            return num_edge
        def get_max_right(root, num_edge=0):
            if root is None:
                return num_edge
            num_edge = get_max_right(root.right, num_edge+1)
            return num_edge
    
    
        if root is None:
            return 0
        max_left = 0 
        max_right = 0 
        print(f'tree: {root}')
        if root.left is not None:
            max_left = get_max_left(root.left, num_edge=1)
        if root.right is not None:
            max_right = get_max_right(root.right, num_edge=1)
        tot_max = max_left + max_right

        print(f'max_left: {max_left}, max_right: {max_right}, tot_max: {tot_max}')

        if root.left is not None:    
            n = root.left
            while n:
                print(f'left root node: {n}')
                max_left = get_max_left(n.left)
                max_right = get_max_right(n.right)
                tot_max = max(max_left + max_right, tot_max)
                n = n.left
        print(f'after left traversal - max is: {tot_max}')
        if root.right is not None:
            n = root.right
            while n:
                print(f'right root node: {n}')
                max_left = get_max_left(n.left)
                max_right = get_max_right(n.right)
                tot_max = max(max_left + max_right, tot_max)
                n = n.right
        print(f'after right traversal - max is: {tot_max}')

        return tot_max




"""
Re-code the traversals
"""

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

def diamter_of_binary_tree(root):
    longest = 0
    def _recurse(root):
        nonlocal longest
        if root is None:
            return 0
        lh = _recurse(root.left)
        rh = _recurse(root.right)
        longest = max(longest, rh+lh)
        return max(lh, rh) + 1
    
    if root is None or (root.left is None and root.right is None):
        return 0
    _recurse(root)
    return longest



"""
TEST CASES
"""

root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right = TreeNode(3)

# print(preorder(root))
# print(postorder(root))
# print(inorder(root))


print(diamter_of_binary_tree(root))

