"""
1.1 Is Unique.

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s):
    """
    Method to determine if a string has all unique characters.

    Using HashMap we have O(n) or O(1) considering ASCII String that will
    run 128 times in worse case.
    Args:
        s: input string.
    Return:
        Boolean: True if string has all unique characters.
    """
    # We can use 255 if is Extended ASCII
    if len(s) > 128:
        return False

    char_set = set()
    for c in s:
        if c in char_set:
            return False
        char_set.add(c)

    return True


def is_unique_with_sort(s):
    """
    Method to determine if a string has all unique characters.

    This is in case that we can't use additional data structures,
    we can get O(n log n).
    Args:
        s: input string.
    Return:
        Boolean: True if string has all unique characters.
    """
    s_sorted = sorted(s)

    for i in range(len(s_sorted) - 1):
        if s_sorted[i] == s_sorted[i + 1]:
            return False

    return True
