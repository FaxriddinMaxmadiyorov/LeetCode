class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col, bound = len(grid), len(grid[0]), 0
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for k in range(4):
                        ii, jj = x[k] + i, y[k] + j
                        if ii < 0 or jj < 0 or ii == row or jj == col or grid[ii][jj] == 0:
                            bound += 1
        return bound