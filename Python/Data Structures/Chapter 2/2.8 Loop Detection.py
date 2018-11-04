"""
2.8 Loop Detection.

Given a circular linked list, implement an algorithm that returns the node at
the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer
points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
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


def loop_detection(head):
    """Method that returns the node at the beginning of the loop."""
    slow = head
    fast = head

    # Find the meeting point. LOOP_SIZE - k steps into the linked list.
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    # Error check - no meeting point, and therefore no loop
    if fast is None or fast.next is None:
        return None

    # Move slow to Head. Keep fast at Meeting Point. Each are k steps from the
    # Loop Start. If they move at the same pace, they must meet at Loop Start.
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    # Both now point to the start of the loop
    return fast
