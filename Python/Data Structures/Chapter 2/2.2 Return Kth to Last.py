"""
2.2 Return Kth to Last.

Implement an algorithm to find the Kth to last element of a singly linked list.
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


def return_kth_to_last(linked_list, k):
    """
    Method to return the kth to last element of a LinkedList.

    The Kth to last element is the (length - k) element. Complexity is
    O(n) time and O(1) space.
    """
    p1 = linked_list
    p2 = linked_list

    for i in range(k):
        if p1 is None:
            return None
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2.data
