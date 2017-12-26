"""
Implement a function to check if a linked list is a palindrome.
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

def palindrome(l):
    """
    We can reverse the list and compare the list with the reverse. O(n)
    """
    reverse_ = reverse(l)
    return l == reverse_

def reverse(l):
    """
    Method to reverse the list. O(n)
    """
    head = Node(l.data)
    while(l.next != None):
        n = Node(l.next.data)
        n.next = head
        head = n
        l = l.next
    return n