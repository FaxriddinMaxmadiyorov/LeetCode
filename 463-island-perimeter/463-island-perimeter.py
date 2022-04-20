class Solution(object):
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        
        rows, cols = len(grid), len(grid[0])
        
        
        def dfs(grid, i, j):
            nonlocal res
            if i<0 or i>rows-1 or j<0 or j>cols-1:
                res += 1
                return 
            
            if grid[i][j] == 0:
                res += 1
                return
            
            if grid[i][j] == -1:
                return
            
            grid[i][j] = -1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(grid, i+dr, j+dc)

            
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(grid, r, c)
                    return res