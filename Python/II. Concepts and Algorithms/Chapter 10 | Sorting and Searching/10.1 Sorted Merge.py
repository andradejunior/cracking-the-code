"""
10.1 Sorted Merge.

You are given two sorted arrays, A and B, where A has a large enough buffer at
the end to hold B. Write a method to merge B into A in sorted order.
"""


def sorted_merge(a, b):
    """Method to merge array B into array A in sorted order."""
    r = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[i])
            j += 1
    r += a[i:]
    r += b[j:]
    return r
