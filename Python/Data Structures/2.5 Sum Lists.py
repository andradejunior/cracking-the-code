"""
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1's digit is at the head
of the list. Write a function that adds the two numbers and returns the sum as a 
linked list.
EXAMPLE
Input:  (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
Input:  (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
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

def sumLists(l1, l2, out=None, r=0):
    """
    We can iterate the two lists and sum the values verifying if there are some Null value.
    O(n) being n the bigger list.
    """
    sum, remainder = 0, 0
    if l1 is None and l2 is None:
        if r != 0:
            out.appendToTail(r)
        return out
    
    if l2 is not None:
        sum += l2.data
        l2 = l2.next
    if l1 is not None:
        sum += l1.data
        l1 = l1.next
    sum += r

    if sum >= 10:
        sum -= 10
        remainder += 1

    if out is None:
        out = Node(sum)
    else:
        out.appendToTail(sum)

    return sumLists(l1, l2, out, remainder)