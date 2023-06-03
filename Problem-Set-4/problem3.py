"""
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]
"""
matrix = [[1,2,3], [4,5,6], [7,8,9]]

def transposeMatrix(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    columns = len(matrix[0])

    transpose = [[i+j for j in range(rows)] for i in range(columns)]

    for i in range(columns):
        for j in range(rows):
            transpose[i][j] = matrix[j][i]

    return transpose

print(transposeMatrix(matrix))
    