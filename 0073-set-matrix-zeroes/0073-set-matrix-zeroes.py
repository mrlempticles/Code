class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """

        m = len(matrix)
        n = len(matrix[0])

        row0 = False
        col0 = False

        # Check if first row contains 0
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True

        # Check if first column contains 0
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Set first row to zero if needed
        if row0:
            for j in range(n):
                matrix[0][j] = 0

        # Set first column to zero if needed
        if col0:
            for i in range(m):
                matrix[i][0] = 0