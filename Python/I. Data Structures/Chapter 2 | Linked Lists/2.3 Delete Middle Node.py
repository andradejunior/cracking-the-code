"""
2.3 Delete Middle Node.

Implement an algorithm to delete a node in the middle(i.e., any node but the
first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.
EXAMPLE
Input: the node c from the linked a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""


class Node:
    """LinkedList Node Class."""

    def __init__(self, d):
        """Init method."""
        self.data = d
        self.next = None

    def append_to_tail(self, d):
        """Method to append to tail of the LinkedList."""
        end = Node(d)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def __str__(self):
        """Method to print the LinkedList."""
        n = self
        s = '[ '
        while(n is not None):
            s = s + str(n.data) + ' '
            n = n.next
        return s + ']'


def delete_node(head, d):
    """Method to delete a node in the LinkedList."""
    n = head
    if n.data == d:
        return head.next
    while n.next is not None:
        if n.next.data == d:
            n.next = n.next.next
            return head
        n = n.next
    return head


def delete_middle_node(n):
    """
    Method to delete a middle node of a LinkedList.

    Just copy the data from the next node over the current node. Complexity is
    O(1).
    """
    if n is None or n.next is None:
        return False  # It's not possible
    next_node = n.next
    n.data = next_node.data
    n.next = n.next.next

    return True
