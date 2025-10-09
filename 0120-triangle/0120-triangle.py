class Solution(object):
    def minimumTotal(self, triangle):
        # Start from the second last row and move upward
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update each element with the min path sum from below
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        # The top element now contains the minimum total
        return triangle[0][0]