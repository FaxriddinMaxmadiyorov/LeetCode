class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        mat = [[0 for j in range(col)] for i in range(row)]
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = 0
                    for k in range(4):
                        if self.inBox(x[k] + i, y[k] + j, row, col) and grid[x[k] + i][y[k] + j] == 1:
                            temp += 1
                    mat[i][j] = temp
        s = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    s += 3
                elif mat[i][j] == 2:
                    s += 2
                elif mat[i][j] == 3:
                    s += 1
        s = 4 if s == 0 else s
        return s
    
    def inBox(self, i, j, n, m):
        if i >= 0 and j >= 0 and i < n and j < m:
            return True
        return False