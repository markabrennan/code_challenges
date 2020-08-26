"""
Tree problem from Leet Code post
about Amazon interview:
https://leetcode.com/discuss/interview-question/797541/amazon-online-assessment-2-sde-1-new-graduate-2021-coding-2-questions-with-solutions

Get highest average of "manager" nodes (nodes with children), 
inclusive of manager and all reports (child nodes).

Note the tree is NOT a BST; each parent node can have
more than two child nodes.
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.children = []


def print_nodes(root):
    vals = []
    def dfs(root):
        nonlocal vals
        if root is None:
            return
        vals.append(root.val)
        for node in root.children:
            dfs(node)
    dfs(root)
    return vals


def count_nodes(root):
    averages = []
    def dfs(root):
        nonlocal averages
        if root is None:
            return 0, 0
        child_count = 0
        child_val = 0
        for node in root.children:
            val, num_children = dfs(node)
            child_count += num_children
            child_val += val
        print(f'level - root.val:  {root.val} | child_count: {child_count} | child_val: {child_val}')
        if child_count != 0:
            child_val += root.val
            child_count += 1
            averages.append((root.val, round(child_val / child_count,3)))
        else:
            child_val += root.val
            child_count += 1
        return child_val, child_count
        
    dfs(root)
    return max(averages, key=lambda x: x[1])[0]



"""
TEST CASES
"""
root = TreeNode(20)

node = TreeNode(11)
node1 = TreeNode(2)
node2 = TreeNode(3)

root_child_left = TreeNode(12)

root_child_left.children.extend([node, node1, node2])

root.children.append(root_child_left)


root_child_right = TreeNode(18)

child1 = TreeNode(15)
child2 = TreeNode(8)

root_child_right.children.extend([child1, child2])

root.children.append(root_child_right)

#print(print_nodes(root))
print(count_nodes(root))