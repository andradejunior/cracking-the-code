"""
Implement an algorithm to find the Kth to last element of a singly linked list.
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

def returnKthToLast(list, k):
	"""
	The Kth to last element is the (length - k) element. O(n) time and O(1) space.
	"""
	p1 = list
	p2 = list

	for i in range(k):
		if p1 is None:
			return None
		p1 = p1.next

	while p1 != None:
		p1 = p1.next
		p2 = p2.next

	return p2.data