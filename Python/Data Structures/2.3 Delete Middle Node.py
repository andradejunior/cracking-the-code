"""
Implement an algorithm to delete a node in the middle(i.e., any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.
EXAMPLE
Input: the node c from the linked a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->
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

def deleteMiddleNode(n):
	"""
	Just copy the data from the next node over the current node. O(1)
	"""
	if n is None or n.next is None:
		return False #It's not possible
		
	next = n.next
	n.data = next.data
	n.next = n.next.next

	return True