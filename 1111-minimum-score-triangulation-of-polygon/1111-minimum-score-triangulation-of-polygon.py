class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # l = length of the interval
        for l in range(3, n + 1):  # at least 3 points to form a triangle
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]
