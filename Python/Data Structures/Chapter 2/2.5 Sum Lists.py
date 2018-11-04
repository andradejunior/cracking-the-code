"""
2.5 Sum Lists.

You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.
EXAMPLE
Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input:  (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
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


def sum_lists(l1, l2, out=None, r=0):
    """
    Method to sum two values stored as a LinkedList.

    We can iterate the two lists and sum the values verifying if there are some
    Null value. Complexity is O(n) being n the bigger list.
    """
    sum_values, remainder = 0, 0
    if l1 is None and l2 is None:
        if r != 0:
            out.append_to_tail(r)
        return out

    if l2 is not None:
        sum_values += l2.data
        l2 = l2.next
    if l1 is not None:
        sum_values += l1.data
        l1 = l1.next
    sum_values += r

    if sum_values >= 10:
        sum_values -= 10
        remainder += 1

    if out is None:
        out = Node(sum_values)
    else:
        out.append_to_tail(sum_values)

    return sum_lists(l1, l2, out, remainder)
