"""
4.2 Minimal Tree.

Given a sorted(incresing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""


class Node:
    """Class that represents a node."""

    def __init__(self, value):
        """Init method."""
        self.value = value
        self.right = None
        self.left = None


def create_minimal_tree(arr):
    """Method to create a binary search tree with minimal height."""
    return minimal_tree(arr, 0, len(arr) - 1)


def minimal_tree(arr, start, end):
    """Method to create a binary search tree with minimal height."""
    if end < start:
        return None
    mid = (start + end) // 2
    n = Node(arr[mid])
    n.left = minimal_tree(arr, start, mid - 1)
    n.right = minimal_tree(arr, mid + 1, end)
    return n
