"""
1.4 Palindrome Permutation.

Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters. The palindrome does not
need to be limited to just dictionary words.
EXAMPLE
Input:  Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""


def palindrome_permutation(s):
    """
    Method to check if the string is a permutation of a palindrome.

    We can put the characters in a HashTable and count, after that we check if
    there are just even values(except for one value in strings of odd lengths).
    Complexity is O(n).
    Args:
        s: input string.
    Return:
        Boolean: True if it is permutation of a palindrome.
    """
    s = s.replace(' ', '').lower()
    count = {}
    odd_flag = False
    if len(s) % 2 != 0:
        odd_flag = True

    for c in s:
        if count.get(c) is not None:
            count[c] = count[c] + 1
        else:
            count[c] = 1

    for v in count.values():
        if v % 2 != 0:
            if odd_flag:
                odd_flag = False
            else:
                return False

    return True
