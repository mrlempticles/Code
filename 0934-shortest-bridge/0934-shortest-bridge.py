
from collections import deque

class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        queue = deque()
        found = False

        # Find the first island using DFS
        def dfs(r, c):
            if (r < 0 or r >= n or c < 0 or c >= n
                    or grid[r][c] != 1):
                return

            grid[r][c] = 2
            queue.append((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Locate any land cell and mark its entire island
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        # Expand from the first island using BFS
        steps = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue

                    if grid[nr][nc] == 1:
                        return steps

                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

            steps += 1

        return -1
