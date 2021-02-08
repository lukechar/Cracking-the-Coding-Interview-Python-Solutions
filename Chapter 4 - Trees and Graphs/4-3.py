# 4-3: List of Depths: Given a binary tree, design an algo which creates a linked list of all the nodes at
# each depth.

import sys

from tree import BinTree, Node

def solution(bin_tree):
    res_list_of_ll = []
    nodes_dict = dict()  # keep track of nodes at each level with hash table (dict)

    # Pre-order traversal, but keep track of depth
    def traverse(root, depth):
        # visit root, add to hash table with level as key
        if depth in nodes_dict:
            nodes_dict[depth].append(root)
        else:
            nodes_dict[depth] = [root]
        if root.left:
            traverse(root.left, depth + 1)
        if root.right:
            traverse(root.right, depth + 1)

    traverse(bin_tree.root, 0)

    # Build linked list for each level in hash table, add to result list of linked lists
    for level in nodes_dict:
        level_list = nodes_dict[level]
        ll = LinkedList(LinkedListNode(level_list[0].value))
        current = ll.head  # pointer for building linked list
        for i in range(1, len(level_list)):
            current.next = LinkedListNode(level_list[i].value)
            current = current.next

        res_list_of_ll.append(ll)  # add this linked list to the result list to be returned

    return res_list_of_ll

# Extend tree.Node class to add marked property
class BinTreeNode(Node):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.marked = False


# Singly Linked List setup
class LinkedList:
    def __init__(self, head):
        self.head = head

    def equals(self, other):
        current = self.head
        current_other = other.head
        while True:
            if current.value != current_other.value:
                return False
            if current.next is None and current_other.next is not None:
                return False
            if current.next is not None and current_other is None:
                return False
            if current.next is None:
                return True
            current = current.next
            current_other = current_other.next

    def __str__(self):
        ll_str = ''
        current = self.head
        while True:
            ll_str += str(current.value)
            if current.next is None:
                break
            current = current.next
            ll_str += ' -> '
        return ll_str

class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

# Test solution
if __name__ == "__main__":

    case_tree = BinTree(Node(5))
    # Left subtree
    case_tree.root.left = Node(3)
    case_tree.root.left.left = Node(2)
    case_tree.root.left.right = Node(4)
    # Right subtree
    case_tree.root.right = Node(7)
    case_tree.root.right.left = Node(6)
    case_tree.root.right.right = Node(8)

    level_0 = LinkedList(LinkedListNode(5))
    level_1 = LinkedList(LinkedListNode(3, LinkedListNode(7)))
    level_2 = LinkedList(LinkedListNode(2, LinkedListNode(4, LinkedListNode(6, LinkedListNode(8)))))

    solution_list_of_ll = [level_0, level_1, level_2]

    try:
        res_list_of_ll = solution(case_tree)
        assert(len(res_list_of_ll) == len(solution_list_of_ll))
        for ll_res, ll_sol in zip(res_list_of_ll, solution_list_of_ll):
            assert(ll_res.equals(ll_sol))
    except AssertionError:
        print('Fail!')
        print('Result: ' + str([str(x) for x in res_list_of_ll]))
        print('Correct: ' + str([str(x) for x in solution_list_of_ll]))
        sys.exit()
    print('Pass!')
    