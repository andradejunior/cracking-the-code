"""
3.2 Stack Min.

How would you design a stack which, in addition to push and pop, has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.
"""


class Stack(list):
    """Stack class using a python list."""

    def __init__(self):
        """Init method."""
        super().__init__()

    def peek(self):
        """Method to return the top of the stack."""
        return self[-1] if len(self) else None

    def pop(self):
        """Method to remove the top item from the stack."""
        return super().pop()

    def push(self, item):
        """Method to add an item to the top of the stack."""
        super().append(item)


class StackWithMin(Stack):
    """Stack with min track."""

    def __init__(self):
        """Init method."""
        super().__init__()
        self.min_stack = Stack()

    def min(self):
        """Method to return the minimum element of the stack."""
        return self.min_stack.peek()

    def pop(self):
        """Method to remove the top item from the stack."""
        item = super().pop()
        auxiliar_stack = Stack()
        while item != self.min_stack.peek():
            auxiliar_stack.push(self.min_stack.pop())
        self.min_stack.pop()
        while auxiliar_stack.peek():
            self.min_stack.push(auxiliar_stack.pop())
        return item

    def push(self, item):
        """Method to add an item to the top of the stack."""
        super().push(item)
        if self.min_stack.peek() is None:
            self.min_stack.push(item)
        else:
            auxiliar_stack = Stack()
            while self.min_stack.peek():
                if item > self.min_stack.peek():
                    auxiliar_stack.push(self.min_stack.pop())
                else:
                    break
            self.min_stack.push(item)
            while auxiliar_stack.peek():
                self.min_stack.push(auxiliar_stack.pop())
