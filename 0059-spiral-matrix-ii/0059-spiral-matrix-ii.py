class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # 1. Fill top row: left -> right
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1

            top += 1

            # 2. Fill right column: top -> bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1

            right -= 1

            # 3. Fill bottom row: right -> left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = num
                    num += 1

                bottom -= 1

            # 4. Fill left column: bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1

                left += 1

        return matrix