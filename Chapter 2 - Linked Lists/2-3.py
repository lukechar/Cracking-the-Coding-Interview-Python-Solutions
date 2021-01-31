# 2.3: Delete a middle (any but first or last) node from a linked list, given access to only the node to be deleted.

def solution(node_to_delete):
    node_to_delete.value = node_to_delete.next.value  # change this node's value to the next node's value
    node_to_delete.next = node_to_delete.next.next  # remove the next node by skipping it

    # We've essentially transformed the node to be deleted into the node following it and removed that
    # following node from the linked list. With a doubly-linked list, we could have gotten the node_to_delete.prev
    # and simply used that pointer to connect node_to_delete.prev.next to node_to_delete.next, removing node_to_delete
    # from the linked list entirely.


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

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

# Test solution
if __name__ == "__main__":

    ll = LinkedList(Node(1))
    ll.head.next = Node(2)
    ll.head.next.next = Node(2)
    ll.head.next.next.next = Node(3)  # to be deleted
    ll.head.next.next.next.next = Node(4)

    ll_deleted_middle_node = LinkedList(Node(1))
    ll_deleted_middle_node.head.next = Node(2)
    ll_deleted_middle_node.head.next.next = Node(2)
    ll_deleted_middle_node.head.next.next.next = Node(4)

    test_cases = {
        ll.head.next.next.next: ll_deleted_middle_node
    }

    fails = 0
    for case in test_cases:
        try:
            solution(case)
            res = ll
            correct = test_cases[case]
            assert(res.equals(correct))
        except AssertionError:
            fails += 1
            print(f'\nCase: {case}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        