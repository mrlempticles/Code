class Solution(object):
    def rangeAddQueries(self, n, queries):
        # Create a 2D difference array
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Apply all queries to the difference array
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Build prefix sums horizontally (row-wise)
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        # Build prefix sums vertically (column-wise)
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Extract the resulting n x n matrix
        res = [[diff[i][j] for j in range(n)] for i in range(n)]
        return res
