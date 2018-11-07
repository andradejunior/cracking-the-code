"""
1.3 URLify.

Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can
perform this operation in place)
EXAMPLE
Input:  "Mr John Smith   ", 13
Output: "Mr%20John%20Smith"
"""


def urlify(s):
    """
    Method to replace all spaces in a string with '%20'.

    We can split the string into a list and join the words puting the
    character '%20' between each word. Complexity is O(n). A less
    pythonic way is do that within a for loop instead of use the method
    join.
    Args:
        s: input string.
    Return:
        output: string with the spaces replaced by '%20'.
    """
    return '%20'.join(s.split())
