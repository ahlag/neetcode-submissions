class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        R, C = len(matrix), len(matrix[0])

        row_cutoff = R // 2
        # col_cutoff = C // 2 if C % 2 == 0 else C // 2 - 1

        for r in range(row_cutoff):
            for c in range(C):
                matrix[r][c], matrix[R- r - 1][c] = matrix[R- r - 1][c], matrix[r][c]

        print(matrix)

        for r in range(R):
            for c in range(r+1, C):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        print(matrix)
        


        