"""
2.4 Partition.

Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater that or equal to x. If x is contained
within the list, the values of x only need to be after the elements less than
x(see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between to appear between the
left and right partitions.
EXAMPLE
Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
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


def linked_list_size(head):
    """Method to return a LinkedList size."""
    length = 0
    n = head
    while n is not None:
        length += 1
        n = n.next
    return length


def partition(l, p):
    """
    Method to partition a LinkedList around a value.

    Iterating over all the list we can append to tail the Nodes that are
    greater or equal the partition, and delete the node. Complexity is O(n).
    """
    length = linked_list_size(l)
    n = l
    for i in range(length):
        if n.data >= p:
            l.append_to_tail(n.data)
            l.delete_node(n.data)
        n = n.next

    return l
