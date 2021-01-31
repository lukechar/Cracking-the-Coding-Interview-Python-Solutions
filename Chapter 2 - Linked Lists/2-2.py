# 2.2: Find the kth to last element of a singly linked list.

# Time complexity: O(n)
# Space complexity: O(n)
def solution(ll, k):
    nodes_array = []
    # Traverse list to determine total number of nodes - add all node values to array
    current = ll.head
    while current:
        nodes_array.append(current.value)
        current = current.next

    # Return kth to last element of nodes array
    n = len(nodes_array)
    return nodes_array[n - k]


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
    ll.head.next.next.next = Node(3)
    ll.head.next.next.next.next = Node(4)
    ll.head.next.next.next.next.next = Node(4)
    ll.head.next.next.next.next.next.next = Node(2)
    ll.head.next.next.next.next.next.next.next = Node(1)
    ll.head.next.next.next.next.next.next.next.next = Node(5)

    test_cases = {
        (ll, 4): 4,
        (ll, 1): 5,
        (ll, 7): 2,
        (ll, 2): 1,
        (ll, 3): 2,
    }

    fails = 0
    for case in test_cases:
        try:
            res = solution(case[0], case[1])
            correct = test_cases[case]
            assert(res == correct)
        except AssertionError:
            fails += 1
            print(f'\nCase: {case}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        