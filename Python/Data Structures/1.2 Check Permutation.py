"""
Given two strings, write a method to decide if one is a permutation of the other.
"""

def checkPermutation(s1, s2):
    """
    We can sort the strings and compare the results. O(n log n)
    """
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    if s1 == s2:
        return True

    return False