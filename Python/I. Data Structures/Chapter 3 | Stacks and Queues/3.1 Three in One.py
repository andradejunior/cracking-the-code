"""
3.1 Three in One.

Describe how you could use a single array to implement three stacks.
"""


class FixedMultiStack:
    """Class for a Fixed Multi Stack."""

    def __init__(self, stack_size):
        """Init method."""
        self.num_stacks = 3
        self.array = [0] * (stack_size * self.num_stacks)
        self.sizes = [0] * self.num_stacks
        self.stack_size = stack_size

    def push(self, item, stack_num):
        """Method to add an item to the top of the stack."""
        if self.is_full(stack_num):
            raise Exception('Stack is full.')
        self.sizes[stack_num] += 1
        self.array[self.index_of_top(stack_num)] = item

    def pop(self, stack_num):
        """Method to remove the top item from the stack."""
        if self.is_empty(stack_num):
            raise Exception('Stack is empty.')
        value = self.array[self.index_of_top(stack_num)]
        self.array[self.index_of_top(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        """Method to return the top of the stack."""
        if self.is_empty(stack_num):
            raise Exception('Stack is empty.')
        return self.array[self.index_of_top(stack_num)]

    def is_empty(self, stack_num):
        """Method to check if the stack is empty."""
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        """Method to verify if the stack is full."""
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        """Method to return the index of the top of the stack."""
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1
