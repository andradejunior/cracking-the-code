"""
1.8 Zero Matrix.

Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column are set to 0. This take O(NM).
"""


def nulify_column(matrix, column):
    """
    Method to set column of a matrix to zero.

    Args:
        matrix: input matrix.
    Returns:
        matrix: matrix with column set to zero.
    """
    for i in range(len(matrix)):
        matrix[i][column] = 0
    return matrix


def nulify_row(matrix, row):
    """
    Method to set row of a matrix to zero.

    Args:
        matrix: input matrix.
    Returns:
        matrix: matrix with row set to zero.
    """
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
    return matrix


def zero_matrix(matrix):
    """
    Method to verify if element is zero and set row and columns to zero.

    Args:
        matrix: input matrix.
    Returns:
        matrix: zero matrix.
    """
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)

    for i in row:
        nulify_row(matrix, row)
    for j in col:
        nulify_column(matrix, j)

    return matrix
