"""
Write code to partition a linked list around a value x, sucj that all nodes less than x come
before all nodes greater that or equal to x. If x is contained within the list, the values 
of x only need to be after the elements less than x (see below). The partition element x
can appear anywhere in the "right partition"; it does not need to appear between to appear
between the left and right partitions.
EXAMPLE
Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
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

def partition(l, p):
    """
    Iterating over all the list we can append to tail the Nodes that are greater or equal the partition, 
    and delete the node. This take O(n).
    """

    length = 0

    n = l
    while (n.next != None):
        length += 1
        n = n.next

    n = l
    for i in range(length):
        if n.data >= p:
            l.appendToTail(n.data)
            l.deleteNode(n.data)
        n = n.next

    return l