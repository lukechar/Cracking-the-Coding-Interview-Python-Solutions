# 3-2: Design a stack which can push, pop and return the minimum element in O(1) time.

class MinStack:
    def __init__(self):
        self.min_items = []  # stack-ception! This internal stack will keep track of the min values.
        self.stack = []

    def pop(self):
        pop_val = self.stack.pop()
        if pop_val in self.min_items:
            self.min_items.remove(pop_val)
        return pop_val

    def push(self, item):
        if not self.min_items or item < self.min_items[-1]:
            self.min_items.append(item)
        self.stack.append(item)

    def min(self):
        return self.min_items[-1]

# Test solution
if __name__ == "__main__":
    stack = MinStack()
    stack.push(3)
    stack.push(7)
    stack.push(-4)

    print(stack.pop()) # should print -4

    stack.push(5)
    stack.push(-2)
    stack.push(4)

    print(stack.min())  # should print -2

    stack.pop()  # remove 4
    stack.pop()  # remove -2

    print(stack.min())  # should print 3