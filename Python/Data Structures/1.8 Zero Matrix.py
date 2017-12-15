"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.
"""

def zeroMatrix(matrix):
	row = []
	col = []

	for i in range(len(matrix)):
		if i in row:
			continue
		for j in range(len(matrix[0])):
			if j in col:
				continue
			if matrix[i][j] == 0:
				row.append(i)
				col.append(j)

	for i in row:
		for j in range(len(matrix[0])):
			matrix[i][j] = 0
	for i in range(len(matrix)):
		for j in col:
			matrix[i][j] = 0

	return matrix