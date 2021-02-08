# 4-2: Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algo to 
# create a binary search tree with minimum height.

import sys

from tree import BinTree, Node

# Note: arr is ordered
def solution(input_arr):

    def create_min_bst_tree(arr):
        if not arr:
            return None  # if arr is empty, return None - this is the recursion base case

        root = Node(arr[len(arr) // 2])  # get center of array and make it the root Node
        root.left = create_min_bst_tree(arr[:len(arr) // 2])  # left half of array
        root.right = create_min_bst_tree(arr[(len(arr) // 2) + 1:])  # right half of array (excluding root element)

        return root

    root_node = create_min_bst_tree(input_arr)  # call the recursive function with the full input array
    return BinTree(root_node)

# Test solution
if __name__ == "__main__":

    solution_tree = BinTree(Node(5))
    # Left subtree
    solution_tree.root.left = Node(3)
    solution_tree.root.left.left = Node(2)
    solution_tree.root.left.right = Node(4)
    # Right subtree
    solution_tree.root.right = Node(7)
    solution_tree.root.right.left = Node(6)
    solution_tree.root.right.right = Node(8)

    # solution_tree.in_order_traversal(print_nodes=True)  # should visit all nodes in order (2 - 8)

    case_arr = [2, 3, 4, 5, 6, 7, 8]

    try:
        res_tree = solution(case_arr)
        assert(res_tree.equals(solution_tree))
    except AssertionError:
        print('Fail!')
        sys.exit()
    print('Pass!')
    