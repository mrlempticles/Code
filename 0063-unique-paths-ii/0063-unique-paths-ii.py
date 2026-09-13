class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        # If starting point is an obstacle
        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                # Skip the starting cell
                if i == 0 and j == 0:
                    continue

                # Obstacle = no path
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                else:
                    # From above
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

                    # From left
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]