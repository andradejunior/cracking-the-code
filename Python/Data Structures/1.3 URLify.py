"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given 
the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can perform this
operation in place)
EXAMPLE
Input:	"Mr John Smith   ", 13
Output: "Mr%20John%20Smith"
"""

def URLify(s):
	"""
	We can split the string into a list and iterate every word in this list checking if 
	is a empty space, if not we concatenate the string with the caracter '%20'. O(n)
	"""
	l = s.split(' ')
	s = ''

	for w in l:
		if w != '' and len(s) != 0:
			s = s + '%20' + w
		elif w != '':
			s = w

	return s