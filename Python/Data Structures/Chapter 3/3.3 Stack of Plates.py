"""
3.3 Stack of Plates.

Imagine a (literal) stack of plates. If the stacks get too high, it might
topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold. Implement a data structure SetOfStacks
that mimics this. SetOfStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity. SetOfStacks.push()
and SetOfStacks.pop() should behave identically to a single stack(that is,
pop() should return the same values as it would if there were just a single
stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a
specific substack.
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


class SetOfStacks:
    """Set of Stacks."""

    def __init__(self, capacity):
        """Init method."""
        self.capacity = capacity
        self.stacks = [Stack()]

    def peek(self):
        """Method to return the top of the set of stacks."""
        return self.stacks[-1].peek() if len(self.stacks) else None

    def pop(self):
        """Method to remove the top item from the set of stacks."""
        item = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return item

    def push(self, item):
        """Method to add an item to the top of the set of stacks."""
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append(Stack())
        self.stacks[-1].push(item)

    def pop_at(self, index):
        """Method to performs a pop operation on a specific substack."""
        item = self.stacks[index].pop()
        if not self.stacks[index]:
            del self.stacks[index]
        return item
