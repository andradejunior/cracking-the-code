"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

def isUnique(s):
	"""
	Using data structure HashMap(dictionary in Python) we have O(n) or O(1) if we consider
	ASCII String that will run 128 times in worse case.
	"""

	if len(s) > 128: # Considering an ASCII String (We can use 255 if is Extended ASCII)
		return False

	dict = {}

	for c in s:
		if dict.get(c):
			return False
		dict.update({c: True})

	return True

def isUniqueWithSort(s):
	"""
	This is in case that we can't use additional data structures, we can get O(n log n)
	"""
	l = sorted(s)

	for i in range(len(l)):
		if ( ( i < len(l) - 1 ) and ( l[i] == l[i + 1]) ):
			return False

	return True