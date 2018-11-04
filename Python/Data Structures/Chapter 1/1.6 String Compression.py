"""
1.6 String Compression.

Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string. You can assume the string has
only uppercase and lowercase letters (a - z).
"""


def string_compression(s):
    """
    Method to perform basic string compression.

    Args:
        s: input string.
    Returns:
        compressed: compressed string.
    """
    compressed = s[0]
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            compressed += str(count) + s[i + 1]
    compressed += str(count)

    if len(s) > len(compressed):
        return compressed

    return s
