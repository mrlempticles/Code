class Solution:
    def pacificAtlantic(self, heights):
        if not heights: 
            return []
        
        m, n = len(heights), len(heights[0])
        
        pac = [[False]*n for _ in range(m)]
        atl = [[False]*n for _ in range(m)]
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, visited):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    if not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)
        
        # Pacific edges
        for i in range(m):
            dfs(i, 0, pac)
        for j in range(n):
            dfs(0, j, pac)
        
        # Atlantic edges
        for i in range(m):
            dfs(i, n-1, atl)
        for j in range(n):
            dfs(m-1, j, atl)
        
        # Result = cells reachable from both
        result = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    result.append([i, j])
        
        return result
