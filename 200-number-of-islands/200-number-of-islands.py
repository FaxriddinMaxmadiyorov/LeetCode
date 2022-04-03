class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def yesno(i, j, m, n):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True
        
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        x_move = [1, -1, 0, 0]
        y_move = [0, 0, 1, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] = '0'
                    x = collections.deque()
                    y = collections.deque()
                    x.append(i)
                    y.append(j)
                    while len(x) != 0:
                        fx, fy = x[len(x) - 1], y[len(y) - 1]
                        x.pop()
                        y.pop()
                        for u in range(4):
                            if yesno(fx + x_move[u], fy + y_move[u], m, n) and grid[fx + x_move[u]][fy + y_move[u]] == '1':
                                x.appendleft(fx + x_move[u])
                                y.appendleft(fy + y_move[u])
                                grid[fx + x_move[u]][fy + y_move[u]] = '0'
        return cnt