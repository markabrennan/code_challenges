"""
Leet Code: 700. Search in a Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    vals = []
    def dfs(root):
        if root is None:
            return
        nonlocal vals
        vals.append(root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return vals

def inorder(root):
    vals = []
    def dfs(root):
        if root is None:
            return
        nonlocal vals
        dfs(root.left)
        vals.append(root.val)
        dfs(root.right)

    dfs(root)
    return vals

def postorder(root):
    vals = []
    def dfs(root):
        if root is None:
            return
        nonlocal vals
        dfs(root.left)
        dfs(root.right)
        vals.append(root.val)

    dfs(root)
    return vals

"""
Important BST functions from Leet Code.

Key concept is that inorder traversal is
an array sorted in ascending order
"""

def inorder(root):
    """
    Leet Code version of inorder - terse and succinct, and
    no need for non-local vals array! Instead, while
    still using DFS recursion, take advantage of Python array
    concatentation syntax: [] + []....
    """
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def successor(root):
    """Based on above concept, "successor" node is the smallest node after
    the current node. So go right first (since the successor is also larger than
    current node), then go left as much as you can (to get the next smallest).
    """
    root = root.right
    while root.left:
        root = root.left
    return root.val


def predecessor(root):
    """Likewise, predecessor node is the largest node BEFORE the current one;
    so it will be smaller than the current, but the largest; so go left, then
    go right as far as you can, descending the tree.
    """
    root = root.left
    while root.right:
        root = root.right
    return root.val


def delete_node(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.right:
            root.val = successor(root)
            root.right = delete_node(root.right, root.val)
        else:
            root.val = predecessor(root)
            root.left = delete_node(root.left, root.val)

    return root



def search_bst(root, val):
    ret_val = None
    def dfs(root, val):
        nonlocal ret_val
        if root is None:
            return
        if root.val == val:
            ret_val = root
            return
        dfs(root.left, val)
        dfs(root.right, val)

    dfs(root, val)
    return ret_val


def search_bst2(root, val):
    """Key mistake in first version (above)
    is that my DFS algo searches the entire tree,
    instead of evaluating the incoming value
    against the values in the left and right subtrees,
    respectively, and then recursing ONLY on one
    of those subtrees!
    """
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search_bst2(root.left, val)
    elif val > root.val:
        return search_bst2(root.right, val)


def search_bst3(root, val):
    """This is the iterative version - taken from
    Leet Code solution.
    """
    while root is not None and root.val != val:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
    return root


"""
Leet Code Problem: 701. Insert into a Binary Search Tree
Note: I had the basic algorithm here, but neglected to save
the return value of the recursive call(s), e.g.,

root.left = insert_node(root.left, val)

And then you return the entire tree from the root at the bottom of the call;
once the recursive calls bubble up, the tree will have the new
node added, and you return the whole thing from the root.

Likewise, for the iterative solution (more verbose), after you go left or right
you ahve to check whether that node is null and if so, set that branch with the
newly created leaf node, then return the whole tree from the root.  Note that in the
    iterative solution you should save the root and iterate over a node set to the root.
"""

def insert_node(root, val):
    if root is None:
        return TreeNode(val=val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    elif val > root.val:
        root.right = insert_node(root.right, val)

    return root


def insert_node2(root, val):
    node = root
    while node is not None:
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val=val)
                return root
            else:
                node = node.left
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val=val)
                return root
            else:
                node = node.right
    return TreeNode(val=val)



def delete_node2(root, val):
    new_root = None
    def rebuild(new_root, root, val):
        if root.val != val:
            new_root = TreeNode(val)
            node.left = rebuild()

def collect_nodes(root,val):
    vals = []
    def _preorder(root, val):
        nonlocal vals
        if root is None:
            return
        if root.val != val:
            vals.append(root.val)
        _preorder(root.left, val)
        _preorder(root.right, val)
        
    _preorder(root, val)
    return vals

def build_tree(vals):
    root = None
    for val in vals:
        root = insert_node(root, val)
    return root


"""
TEST CASES
"""

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)


print(inorder(root))
print(preorder(root))
print(postorder(root))

#print(preorder(search_bst(root, 4)))
#print(preorder(search_bst3(root, 5)))

#new_root = insert_node2(root, 5)

#vals = collect_nodes(root, 2)
# print(vals)

# print(preorder(build_tree(vals)))

new_root = delete_node(root, 2)
print(inorder(new_root))
print(preorder(new_root))
print(postorder(new_root))
