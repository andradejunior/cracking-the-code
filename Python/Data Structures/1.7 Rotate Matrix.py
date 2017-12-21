"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotateMatrix(matrix):
    """
    We perform circular rotation in each layer, moving the top edge to the right edge, the right
    edge to the bottom edge, the bottom edge to the left edge, and the left edge to the top edge.
    This take O(n^2).
    """
    n = len(matrix)

    for layer in range(len(matrix)//2):

        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] # save top

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top # right <- saved top
            

    return matrix