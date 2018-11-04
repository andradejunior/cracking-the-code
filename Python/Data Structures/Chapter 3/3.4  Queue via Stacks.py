"""
3.4 Queue via Stacks.

Implement a MyQueue class which implements a queue using two stacks.
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


class MyQueue():
    """Queue class using two stacks."""

    def __init__(self):
        """Init method."""
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def add(self, item):
        """Method to add a item to the end of the queue."""
        self.stack_newest.push(item)

    def remove(self):
        """Method to remove the first item in the queue."""
        self.shift_stacks()
        return self.stack_oldest.pop()

    def is_empty(self):
        """Method to check if the queue is empty."""
        return self.stack_newest.is_empty() or self.stack_oldest.is_empty()

    def shift_stacks(self):
        """Method to move elements from stack_newest from stack_oldest."""
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())
