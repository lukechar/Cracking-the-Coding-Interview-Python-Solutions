# 4-5: Validate BST: Implement a function to check if a binary tree is a binary search tree.

from tree import BinTree, Node

def solution(tree_to_check):

    # Traverse entire tree (pre-order), check if current node's children (if they exist) and check that 
    # its left child is less than or equal to this node and right child is greater than this node.
    def visit(root):
        left_res = True
        right_res = True
        if root.left:
            if root.left.value > root.value:
                return False
            left_res = visit(root.left)
        if root.right:
            if root.right.value <= root.value:
                return False
            right_res = visit(root.right)
        return left_res and right_res

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

    tree_2 = BinTree(Node(8))
    # Left subtree
    tree_2.root.left = Node(3)
    tree_2.root.left.left = Node(2)
    tree_2.root.left.right = Node(4)
    # Right subtree
    tree_2.root.right = Node(7)
    tree_2.root.right.left = Node(6)
    tree_2.root.right.right = Node(8)

    tree_3 = BinTree(Node(10))
    # Left subtree
    tree_3.root.left = Node(8)
    tree_3.root.left.left = Node(6)
    tree_3.root.left.right = Node(9)
    # Right subtree
    tree_3.root.right = Node(12)
    tree_3.root.right.left = Node(11)
    tree_3.root.right.right = Node(13)

    tree_4 = BinTree(Node(10))
    # Left subtree
    tree_4.root.left = Node(8)
    tree_4.root.left.left = Node(6)
    tree_4.root.left.right = Node(9)
    # Right subtree
    tree_4.root.right = Node(12)
    tree_4.root.right.left = Node(11)
    tree_4.root.right.left.left = Node(14)
    tree_4.root.right.right = Node(13)


    test_cases = {
        tree_1: True,
        tree_2: False,
        tree_3: True,
        tree_4: False,
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
    