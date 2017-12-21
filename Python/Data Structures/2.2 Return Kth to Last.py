"""
Implement an algorithm to find the Kth to last element of a singly linked list.
"""

def kthToLast(list, k):
	"""
	The Kth to last is the (length - k) element. O(1)
	"""
	if k != 0:
		return list[len(list) - k]
	else:
		return list[len(list)]