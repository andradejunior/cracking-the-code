"""
3.5 Sort Stack.

Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure(such as an array). The stack supports the
following operations: push, pop, peek, and isEmpty.
"""


class Stack(list):
    """Stack class using a python list."""

    def __init__(self):
        """Init method."""
        super().__init__()

    def is_empty(self):
        """Check if stack is empty."""
        return not self

    def peek(self):
        """Method to return the top of the stack."""
        return self[-1] if len(self) else None

    def pop(self):
        """Method to remove the top item from the stack."""
        return super().pop()

    def push(self, item):
        """Method to add an item to the top of the stack."""
        super().append(item)


def sort_stack(stack):
    """Method to sort a stack."""
    sorted_stack = Stack()
    sorted_stack.push(stack.pop())

    while not stack.is_empty():
        temp = stack.pop()
        while not sorted_stack.is_empty() and temp > sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    return sorted_stack
