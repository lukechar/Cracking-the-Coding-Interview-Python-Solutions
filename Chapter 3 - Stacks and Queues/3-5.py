# 3-5: Write a program to sort a stack such that the smallest items are on the top. You can use an
# additional temporary stack, but not any other data structures, such as an array. The stack supports
# push, pop, peek and isEmpty.

from random import randint

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack

    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    res_stack = Stack()
    temp_stack = Stack()
    init_stack = Stack()  # this stack will be the same as temp_stack initially and is just to check the final answer

    # Populate temp_stack with random values to sort
    for _ in range(20):
        x = randint(-10, 10)
        temp_stack.push(x)
        init_stack.push(x)

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # SOLUTION
    while temp_stack.peek() is not None:
        temp = temp_stack.pop()
        while res_stack.peek() is not None and res_stack.peek() < temp:
            temp_stack.push(res_stack.pop())
        res_stack.push(temp)

    print(res_stack)  # should print an ordered stack, with min values on top (i.e. descending order)

    # Check answer
    try:
        assert(res_stack.stack == sorted(init_stack.stack, reverse=True))
        print('Correct! :D')
    except AssertionError:
        print('Wrong!')
