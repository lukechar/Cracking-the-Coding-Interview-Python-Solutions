# 4-4: Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this
# question, a balanced tree is defined as a tree s.t. the heights of the subtrees of any node never differ
# by more than one.

from tree import BinTree, Node

def solution(tree_to_check):
    # Recursive function to get max height of subtrees of any node
    def get_height(root):
        if not root:  # base case
            return 0
        return max(get_height(root.left), get_height(root.right)) + 1

    # Traverse entire tree (post-order), get height of each node's subtrees and check if they differ more than 1
    def visit(root):
        if root.left: 
            visit(root.left)
        if root.right:
            visit(root.right)
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if abs(left_height - right_height) > 1:
            return False
        return True

    # Kick-off traversal with root node of tree
    return visit(tree_to_check.root)

# Test solution
if __name__ == "__main__":

    tree_1 = BinTree(Node(5))
    # Left subtree
    tree_1.root.left = Node(3)
    tree_1.root.left.left = Node(2)
    tree_1.root.left.right = Node(4)
    # Right subtree
    tree_1.root.right = Node(7)
    tree_1.root.right.left = Node(6)
    tree_1.root.right.right = Node(8)

    tree_2 = BinTree(Node(5))
    # Left subtree
    tree_2.root.left = Node(3)
    tree_2.root.left.left = Node(2)
    tree_2.root.left.right = Node(4)
    # Right subtree
    tree_2.root.right = Node(7)
    tree_2.root.right.left = Node(6)
    tree_2.root.right.right = Node(8)
    tree_2.root.right.right.left = Node(9)
    tree_2.root.right.right.left.left = Node(10)
    tree_2.root.right.right.left.left.right = Node(11)
    
    tree_3 = BinTree(Node(5))
    # Left subtree
    tree_3.root.left = Node(3)
    tree_3.root.left.left = Node(2)
    tree_3.root.left.right = Node(4)
    # Right subtree
    tree_3.root.right = Node(7)
    tree_3.root.right.left = Node(6)
    tree_3.root.right.right = Node(8)
    tree_3.root.right.right.left = Node(9)
    tree_3.root.right.right.right = Node(14)
    tree_3.root.right.right.left.left = Node(10)
    tree_3.root.right.right.left.right = Node(12)
    tree_3.root.right.right.right.left = Node(16)
    tree_3.root.right.right.right.right = Node(17)

    tree_4 = BinTree(Node(5))
    # Left subtree
    tree_4.root.left = Node(3)
    tree_4.root.left.left = Node(2)
    tree_4.root.left.left.left = Node(19)
    tree_4.root.left.right = Node(4)
    # Right subtree
    tree_4.root.right = Node(7)
    tree_4.root.right.left = Node(6)
    tree_4.root.right.left.right = Node(13)
    tree_4.root.right.right = Node(8)
    tree_4.root.right.right.left = Node(9)
    tree_4.root.right.right.right = Node(14)
    tree_4.root.right.right.left.left = Node(10)
    tree_4.root.right.right.left.right = Node(12)
    tree_4.root.right.right.right.left = Node(16)
    tree_4.root.right.right.right.right = Node(17)


    test_cases = {
        tree_1: True,
        tree_2: False,
        tree_3: False,
        tree_4: True,
    }

    any_failed = False

    try:
        for case in test_cases:
            res = solution(case)
            assert(res == test_cases[case])
    except AssertionError:
        print(f'Test {str(case)} failed. Got {res}, should be {test_cases[case]}.')
        any_failed = True

    if not any_failed:
        print('All tests passed! :D')
    