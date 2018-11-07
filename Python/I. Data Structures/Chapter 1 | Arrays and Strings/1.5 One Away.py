"""
1.5 One Away.

There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write
a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple   -> true
pales, pale -> true
pale, bale  -> true
pale, bake  -> false
"""


def one_away(s1, s2):
    """
    Method to check if two strings are one(or zero edits) away.

    We take O(n) by iterate the entire string and compare with the other, if
    both have same length we just look if there are some replace and if have
    different lengths we compare if there are inserts or removes.
    Args:
        s1: 1st input string.
        s2: 2nd input string.
    Return:
        Boolean: True if the string are one(or zero edits) away.
    """
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) > len(s2):
        return one_edit_insert_or_remove(s1, s2)
    else:
        return one_edit_insert_or_remove(s2, s1)


def one_edit_insert_or_remove(s1, s2):
    """
    Check if strings with differents sizes are one insert or remove away.

    Args:
        s1: 1st input string(Bigger).
        s2: 2nd input string(Smaller).
    Return:
        Boolean: True if the string are one insert or remove away.
    """
    i1 = 0
    i2 = 0
    edit = False
    while i2 < len(s2):
        if s1[i1] != s2[i2]:
            if edit:
                return False
            edit = True
            i1 = i1 + 1

        i1 = i1 + 1
        i2 = i2 + 1

    return True


def one_edit_replace(s1, s2):
    """
    Check if strings with equals sizes are one edit away.

    Args:
        s1: 1st input string.
        s2: 2nd input string.
    Return:
        Boolean: True if the string are one(or zero edits) away.
    """
    edit = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if edit:
                return False
            edit = True

    return True
