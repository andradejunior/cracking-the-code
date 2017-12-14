"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word
or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The 
palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input:	Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""

def palindromePermutation(s):
	"""
	We can put the characters in a HashTable and count, after that we check if there are just even values
	(except for one value in strings of odd lengths). O(n)
	"""
	s = s.replace(' ', '').lower()
	dict = {}
	odd_flag = False
	if len(s) % 2 != 0:
		odd_flag = True

	for c in s:
		if dict.get(c) is not None:
			dict[c] = dict[c] + 1
		else:
			dict[c] = 1

	for v in dict.values():
		if v % 2 != 0:
			if odd_flag:
				odd_flag = False
			else:
				return False

	return True