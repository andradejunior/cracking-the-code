"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or
replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple   -> true
pales, pale -> true
pale, bale  -> true
pale, bake  -> false
"""

def oneWay(s1, s2):
	"""
	We take O(n) by iterate the entire string and compare with the other, if both have same length
	we just look if there are some replace and if have different lengths we compare if there are
	inserts or removes.
	"""

	if abs(len(s1) - len(s2)) > 1:
		return False

	if len(s1) == len(s2):
		return oneEditReplace(s1, s2)
	elif len(s1) > len(s2):
		return oneEditInsertOrRemove(s1, s2)
	else:
		return oneEditInsertOrRemove(s2, s1)

def oneEditInsertOrRemove(s1, s2): # s1 is the bigger and s2 is the smaller
	"""
	Check if there are one remove or one insert by iterate the smaller string  and compare with
	the character of the bigger string.
    """
	i_s1 = 0
	i_s2 = 0
	edit = False
	while i_s2 < len(s2):
		if s1[i_s1] != s2[i_s2]:
			if edit:
				return False
			edit = True
			i_s1 = i_s1 + 1

		i_s1 = i_s1 + 1
		i_s2 = i_s2 + 1

	return True

def oneEditReplace(s1, s2):
	"""
	Check if there are one replace by compare each character in both strings
	"""
	edit = False
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			if edit:
				return False
			edit = True

	return True