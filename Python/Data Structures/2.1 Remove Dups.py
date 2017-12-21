"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

def removeDumps(list):
	"""
	We can use a HashTable to store the items of the list and verify if they alrealdy exists.O(n)
	"""
	dict = {}
	for x in list:
		if dict.get(x) is not None:
			list.remove(x)
		else:
			dict[x] = True
	return list

def removeDumpsWithoutTempBuffer(list):
	"""
	If we can't use temporary buffer we can use two pointers to the list,
	but the first in one position above the other. This take 
	O(1) space complexity but O(n^2) time complexity.
	"""
	i = 1
	for x in list[:-1]:
		for y in list[i:]:
			if x == y:
				print(x, y)
				list.remove(y)
		i = i + 1
	return list