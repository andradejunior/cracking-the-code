"""
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points
to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input:  A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
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

def loopDetection(head):

    slow = head
    fast = head

    # Find the meeting point. This will be LOOP_SIZE - k steps into the linked list.
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