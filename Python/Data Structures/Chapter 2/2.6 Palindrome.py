"""
2.6 Palindrome.

Implement a function to check if a linked list is a palindrome.
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

    def __eq__(self, other):
        """Method to compare if two LinkedLists are equals."""
        n1 = self
        n2 = other
        while n1 is not None:
            if n2 is None or n1.data != n2.data:
                return False
            n1 = n1.next
            n2 = n2.next
        return True


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


def palindrome(l):
    """
    Method to verify if the LinkedList is a palindrome.

    We can reverse the list and compare the list with the reversed list.
    Complexity is O(n).
    """
    reversed_l = reverse(l)
    return l == reversed_l


def reverse(l):
    """
    Method to reverse the list.

    Complexity is O(n).
    """
    head = Node(l.data)
    while l.next is not None:
        n = Node(l.next.data)
        n.next = head
        head = n
        l = l.next
    return n
