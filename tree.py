
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return self.__str__()


def add_node(root, val):
    if root is None:
        print(f'root is None - adding {val}')
        root = TreeNode(val)
        print(f'leaf is now: {root}')
    elif val > root.val:
        print(f'root val is: {root.val}; adding right')
        root.right = add_node(root.right, val)
    else:
        print(f'root val is: {root.val}; adding left')
        root.left = add_node(root.left, val)

    print(f'returning root from add_node')
    return root


def inorder(root, vals):
    if root.left is not None:
        inorder(root.left, vals)

    vals.append(root.val)

    if root.right is not None:
        inorder(root.right, vals)

    return vals

def preorder(root, vals):
    if root is not None:
        vals.append(root.val)
    if root.left is not None:
        preorder(root.left, vals)

    if root.right is not None:
        preorder(root.right, vals)

    return vals


def postorder(root, vals):
    if root.left is not None:
        postorder(root.left, vals)
    if root.right is not None:
        postorder(root.right, vals)

    vals.append(root.val)


global_height = 0
def postorder_height(root):
    global global_height

    if root is None:
        return 0

    lh = postorder_height(root.left)
    rh = postorder_height(root.right)

    global_height = max(global_height, lh + rh + 1)

    return max(lh, rh) + 1

def get_max_height(root):
    global global_height

    postorder_height(root)
    return global_height - 1


global_tree_depth = 0
def get_tree_depth(root):
    global global_tree_depth

    if root is None:
        return 0

    lh = get_tree_depth(root.left)
    rh = get_tree_depth(root.right)

    global_tree_depth = max(global_tree_depth, lh, rh)
    
    return max(lh, rh) + 1


global_tree_depth = 0
global_flag = True
def measure_tree_depth(root):
    global global_tree_depth
    global global_flag

    if root is None:
        return 0

    lh = measure_tree_depth(root.left)
    rh = measure_tree_depth(root.right)

    if lh > rh + 1 or rh > lh + 1:
        global_flag = False
        
    return max(lh, rh) + 1

def measure_tree_depth_wrapper(root):
    measure_tree_depth(root)
    return global_flag


def get_tree_depth_wraper(root):
    get_tree_depth(root)
    return global_tree_depth



def depth_wrapper(root):
    postorder_height(root)
    return global_height - 1


def get_max_num_edge(root, num_edge=0):
    left = get_max_left(root.left)
    right = get_max_right(root.right)

    print(f'left: {left}, right: {right}')

    return left + right

def walk_tree_get_depth(root):
    mx_height = get_max_depth(root)
    if root.left is not None:
        res = 0
        n = root.left
        while n:
            res = get_max_depth(n)
            mx_height = max(res, mx_height)
            n = n.left
    if root.right is not None:
       res = 0
       n = root.right
       while n:
           res = get_max_depth(n)
           n = n.right 

    return mx_height

def get_max_depth(root, visit_count=0, mx=0):
    if root.left is not None:
        visit_count = get_max_depth(root.left, visit_count+1)
        print(f'after traversing left: height: {visit_count}')
    if root.right is not None:
        visit_count = get_max_depth(root.right, visit_count+1)
        print(f'after traversing right: height: {visit_count}')

    # if root.right is not None:
    #     height += get_max_depth(root.right, height+1, mx)
    # print(f'after traversing right: height: {height}')
    # mx = max(mx, lh+rh)
    # print(f'cur max is: {mx}')

    return visit_count

def get_max_edge(root):
    max_left = 0 
    max_right = 0 
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


#global_match = False
def find_node(root, node):
    global global_match
    if root.val == node.val:
        global_match = True
        print('found it')
        print(root.val)
        if root.left is not None: 
            if node.left is not None:
                find_node(root.left, node.left)
            else:
                global_match = False
        elif node.left is not None:
            global_match = False
            
        if root.right is not None:
            if node.right is not None:
                find_node(root.right, node.right)
            else:
                global_match = False
        elif node.right is not None:
            global_match = False
        

    if root.left is not None:
        find_node(root.left, node)
    if root.right is not None:
        find_node(root.right, node)

    return global_match


def find_sub(root, node):
    ret = None
    if root and node:
        if root.val == node.val:
            ret =  root
        if root.left is not None:
            ret = find_sub(root.left, node)
        if ret is None and root.right is not None:
            ret = find_sub(root.right, node)
    return ret

is_subtree = True
def identical(root, node):
    global is_subtree
    if root and node:
        if root.val == node.val:
#            is_subtree = True
            identical(root.left, node.left)
            identical(root.right, node.right)
        elif root.val != node.val:
            is_subtree = False
            return
    elif (root is None and node is not None) or (node is None and root is not None):
        is_subtree = False

def isSubtree(s, t):
    global is_subtree
    sub_root = find_sub(s, t)

    if sub_root is None:
        return False

    identical(sub_root, t)

    return is_subtree

    
            

global_match = False
lh_ret = rh_ret = False
def find_node2(root, node):
    global lh_ret
    global rh_ret
    if root is None and node is None:
        return True
    if (root is None and node is not None) or (node is None and root is not None):
        return False

    if root and node:
        # if root.val != node.val:
        #     return False
        if root.val == node.val:
            lh_ret = find_node2(root.left, node.left)
            rh_ret = find_node2(root.right, node.right)
            return lh_ret and rh_ret
        else:
            return False

#    lh_ret = rh_ret = True
    if root.left is not None:
        lh_ret = find_node2(root.left, node)
    if root.right is not None:
        rh_ret = find_node2(root.right, node)

    return lh_ret and rh_ret


def find_node3(root, node):
    if root and node:
        if root.val == node.val:
            return root
        e


def make_test_tree1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    return root


def make_test_tree2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.right.right.right = TreeNode(7)
    root.left.right.right.right.right = TreeNode(8)

    root.right = TreeNode(3)

    return root


def make_test_tree3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(5)

    return root

def make_test_tree4():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)

    return root

def parts(l):
    root_ix = len(l) // 2
    root = l[root_ix]
    right = l[root_ix+1:]
    left = l[0:root_ix]
    return root, left, right


def addnode(l):
    # code used to solve Leet Code problem # 108
    if len(l) < 1:
        return None
    if len(l) == 1:
        return TreeNode(l[0])
    m = len(l) // 2
    mid = l[m]
    left = l[0:m]
    right = l[m+1:]
    node = TreeNode(mid)
    node.left = addnode(left)
    node.right = addnode(right)
    return node


def build_array_from_ll(L):
    val_list = []
    val_list.append(L.data)
    n = L.next
    while n is not None:
        val_list.append(n.data)
        n = n.next

    return val_list


def add(head, data):
    new_node = Node(data)
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = new_node


def printl(L):
    vals = []
    vals.append(L.data)
    n = L.next
    while n:
        vals.append(n.data)
        n = n.next
    print(vals)

def make_test_tree5():
    t = TreeNode(1)

    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.left = TreeNode(3)

    t.right = TreeNode(2)
    t.right.right = TreeNode(3)

    t.left.left.left = TreeNode(4)

    t.right.right.right = TreeNode(4)

    return t


if __name__ == "__main__":
    t5 = make_test_tree5()
    measure_tree_depth_wrapper(t5)



    # t2 = make_test_tree2()
    # get_tree_depth_wraper(t2)


    # root = TreeNode(0)
    # add_node(root, -3)
    # add_node(root, -10)
    # add_node(root, 9)
    # add_node(root, 5)

    # # vals = inorder(root)
    # # print(vals)

    # test_list = [0, 1, 2, 3, 4, 5]

    # root = addnode(test_list)

    # new_list = [-10, -3, 0, 5, 9]
    # lst = Node(new_list[0])

    # for i in new_list[1:]:
    #     add(lst, i)

    # s = TreeNode(3)
    # s.left = TreeNode(4)
    # s.right = TreeNode(5)
    # s.left.left = TreeNode(1)
    # s.left.right = TreeNode(2)
    # s.left.left.left = TreeNode(0)

    # t = TreeNode(4)
    # t.left = TreeNode(1)
    # t.right = TreeNode(2)

    # s = TreeNode(1)
    # t = TreeNode(0)

    
    # s = TreeNode(3)
    # s.left = TreeNode(4)
    # s.right = TreeNode(5)
    # s.left.left = TreeNode(1)
    # s.left.right = TreeNode(2)

    # t = TreeNode(4)
    # t.left = TreeNode(1)
    # t.right = TreeNode(2)

    s = TreeNode(1)
    s.left = TreeNode(1)
    t = TreeNode(1)

    print(isSubtree(s, t))