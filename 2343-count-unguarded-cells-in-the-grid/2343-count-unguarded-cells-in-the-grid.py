class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0] * n for _ in range(m)]
        
        # Mark guards as 1, walls as 2
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        
        guarded = [[False] * n for _ in range(m)]
        
        # Directions: up, down, left, right
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        
        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                # Continue until blocked
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 2:   # wall
                        break
                    if grid[nr][nc] == 1:   # another guard
                        break
                    
                    guarded[nr][nc] = True
                    nr += dr
                    nc += dc
        
        # Count cells that are empty AND unguarded
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and not guarded[r][c]:
                    ans += 1
        
        return ans
