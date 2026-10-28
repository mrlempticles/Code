
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)

        dp = [row[:] for row in matrix]

        for i in range(1, n):
            for j in range(n):
                up = dp[i - 1][j]

                left = dp[i - 1][j - 1] if j > 0 else float('inf')
                right = dp[i - 1][j + 1] if j < n - 1 else float('inf')

                dp[i][j] += min(up, left, right)

        return min(dp[n - 1])
