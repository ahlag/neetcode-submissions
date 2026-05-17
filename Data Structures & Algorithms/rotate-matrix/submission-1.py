class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # Tranpose matrix

        n_rows, n_cols = len(matrix), len(matrix[0])

        for i in range(n_rows):
            for j in range(i + 1, n_cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()
