"""
1.2 Check Permutation.

Given two strings, write a method to decide if one is a
permutation of the other.
"""


def check_permutation(s1, s2):
    """
    Method to check permutation between two strings.

    We can sort the strings and compare the results. Complexity is O(n log n).
    Args:
        s1: 1st input string.
        s2: 2nd input string.
    Return:
        Boolean: True if string is a permutation of the other.
    """
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)
