"""
2.1 Remove Dups.

Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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


def remove_dups(linked_list):
    """
    Method to remove duplicates from a LinkedList.

    We can use a HashTable to store the items of the list and verify if they
    alrealdy exists. Complexity is O(n).
    """
    temp_buffer = set()
    x = linked_list
    while x is not None:
        if x.data in temp_buffer:
            linked_list = delete_node(linked_list, x.data)
        else:
            temp_buffer.add(x.data)
        x = x.next
    return linked_list


def remove_dups_without_temp_buffer(linked_list):
    """
    Method to remove duplicates from a LinkedList.

    If we can't use temporary buffer we can use two pointers to the list,
    but the first in one position above the other. This take
    O(1) space complexity but O(n^2) time complexity.
    """
    current = linked_list
    while current is not None:
        runner = current.next
        while runner is not None:
            if current.data == runner.data:
                linked_list = delete_node(linked_list, runner.data)
            runner = runner.next
        current = current.next
    return linked_list
