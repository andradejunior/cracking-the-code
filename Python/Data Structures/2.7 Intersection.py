"""
Given two (Singly) linked lists, determine if the two lists intersect. Return the intersecting node.
Note that the intersection is defined based on reference, not value. That is, if the Kth node of the
first linked list is the exact same node (by reference) as the Jth node of the second linked list,
then they are intersecting.
"""
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def appendToTail(self, d):
        end = Node(d)
        n = self
        while(n.next is not None):
            n = n.next
        n.next = end

    def deleteNode(head, d):
        n = head
        if n.data == d:
            return head.next
        while n.next is not None:
            if n.next.data == d:
                n.next = n.next.next
                return head
            n = n.next
        return head

    def __str__(self):
        n = self
        s = '[ '
        while(n is not None):
            s = s + str(n.data) + ' '
            n = n.next
        return s + ']'

    def __eq__(self, other):
        n1 = self
        n2 = other
        while(n1 is not None):
            if n2 is None or n1.data != n2.data:
                return False
            n1 = n1.next
            n2 = n2.next
        return True

def intersection(l1, l2):
    """
    We can iterate over the two lists independently and check if have intersection
    by reference, not by value. O(n)
    """
    if l1 is None or l2 is None:
        return False
    if l1 is l2: # "is" can compare if both are the same object
        return True
    else:
        return intersection(l1.next, l2) or intersection(l1, l2.next)