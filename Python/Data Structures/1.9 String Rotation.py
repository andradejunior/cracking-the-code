"""
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write a code to check if s2 is a rotation of s1 using only
one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
"""

def stringRotation(s1, s2):
    """
    We can check if s1 is substring of the concatenation of s2 + s2.
    Example:
    Input: "waterbottle" and "erbottlewat"
    Check if "waterbottle" is in "erbottlewaterbottlewat"
    Output: True
    """

    if len(s1) == len(s2):
        return isSubstring(s1, s2 + s2)

    return False

def isSubstring(s1, s2):
    """
    Check if s1 is a substring of s2.
    """
    
    return s1 in s2