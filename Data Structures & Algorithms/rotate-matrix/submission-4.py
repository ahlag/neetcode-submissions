class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        R, C = len(matrix), len(matrix[0])

        for r in range(R // 2):
            for c in range(C):
                matrix[r][c], matrix[R- r - 1][c] = matrix[R- r - 1][c], matrix[r][c]

        for r in range(R):
            for c in range(r+1, C):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        


        