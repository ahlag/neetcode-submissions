class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            
            # go right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # go down
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # go left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # go up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res
