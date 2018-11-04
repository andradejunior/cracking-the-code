"""
1.9 String Rotation.

Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write a code to check if s2 is a
rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
rotation of "erbottlewat")
"""


def string_rotation(s1, s2):
    """
    Method to check if one string is a rotation of the other.

    We can check if s1 is substring of the concatenation of s2 + s2.
    Example:
    Input: "waterbottle" and "erbottlewat"
    Check if "waterbottle" is in "erbottlewaterbottlewat"
    Output: True
    Args:
        s1: 1st input string.
        s2: 2nd input string.
    Returns:
        Boolean: True if s1 is a substring of s2.
    """
    if len(s1) == len(s2):
        return is_substring(s1, s2 + s2)

    return False


def is_substring(s1, s2):
    """
    Check if s1 is a substring of s2.

    Args:
        s1: 1st input string.
        s2: 2nd input string.
    Returns:
        Boolean: True if s1 is a substring of s2.
    """
    return s1 in s2
