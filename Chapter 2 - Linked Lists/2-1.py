# 2.1: Write code to remove duplicates from an unsorted linked list. How would you solve this problem if a
# temporary buffer is not allowed?

# Time complexity: O(n)
# Space complexity: O(n)
def solution(ll):
    res_ll = LinkedList(Node(ll.head.value))  # create new LL with same head value as LL passed in

    current = ll.head
    current_res = res_ll.head
    all_vals = set()  # store values encountered as we traverse the LL
    all_vals.add(ll.head.value)

    while current:  # loop until we reach the end of the LL
        
        if current.value not in all_vals:  # check hash table for value, if new value, add to new LL
            current_res.next = Node(current.value)
            current_res = current_res.next
            all_vals.add(current.value)

        current = current.next

    return res_ll

# Time complexity: O(n^2)
# Space complexity: O(1)
def solution_nobuffer(ll):
    current = ll.head  # start primary pointer at head
    while current:
        dup_searcher = current  # secondary pointer
        while dup_searcher.next:
            if dup_searcher.next.value == current.value:
                dup_searcher.next = dup_searcher.next.next  # remove dup_searcher.next Node from linked list
            
            dup_searcher = dup_searcher.next

        current = current.next

    return ll

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

    duplicate_ll = LinkedList(Node(1))
    duplicate_ll.head.next = Node(2)
    duplicate_ll.head.next.next = Node(2)
    duplicate_ll.head.next.next.next = Node(3)
    duplicate_ll.head.next.next.next.next = Node(4)
    duplicate_ll.head.next.next.next.next.next = Node(4)
    duplicate_ll.head.next.next.next.next.next.next = Node(2)
    duplicate_ll.head.next.next.next.next.next.next.next = Node(1)
    duplicate_ll.head.next.next.next.next.next.next.next.next = Node(5)

    nonduplicate_ll = LinkedList(Node(1))
    nonduplicate_ll.head.next = Node(2)
    nonduplicate_ll.head.next.next = Node(3)
    nonduplicate_ll.head.next.next.next = Node(4)
    nonduplicate_ll.head.next.next.next.next = Node(5)

    test_cases = {
        duplicate_ll: nonduplicate_ll,
    }

    fails = 0
    for case in test_cases:
        try:
            print('Testing solution with hash table...')
            res = solution(case)
            correct = test_cases[case]
            assert(res.equals(correct))

            print('Testing solution with no buffer...')
            res = solution_nobuffer(case)
            correct = test_cases[case]
            assert(res.equals(correct))
        except AssertionError:
            fails += 1
            print(f'\nCase: {case}\nSolution returned: {res}\nCorrect Answer: {correct}\n')
    if fails:
        print(f'\n{fails} tests failed.\n')
    else:
        print('\nAll cases passed! :D\n')
        