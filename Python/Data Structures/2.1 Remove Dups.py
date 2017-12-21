"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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

def removeDumps(list):
	"""
	We can use a HashTable to store the items of the list and verify if they alrealdy exists.O(n)
	"""
	dict = {}
	x = list
	while x is not None:
		if dict.get(x.data) is not None:
			list = Node.deleteNode(list, x.data)
		else:
			dict[x.data] = True
		x = x.next
	return list

def removeDumpsWithoutTempBuffer(list):
	"""
	If we can't use temporary buffer we can use two pointers to the list,
	but the first in one position above the other. This take 
	O(1) space complexity but O(n^2) time complexity.
	"""
	i = 1
	x = list
	while x is not None:
		y = x.next
		while y is not None:
			if x.data == y.data:
				list = Node.deleteNode(list, y.data)
			y = y.next
		x = x.next
	return list