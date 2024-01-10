dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        color = [[0 for _ in range(c)] for _ in range(r)]

        def call(x, y):
            color[x][y] = 1

            for dxx, dyy in zip(dx, dy):
                vx = x + dxx
                vy = y + dyy

                if vx < 0 or vy < 0 or vx >= r or vy >= c:
                    continue
                
                if grid[vx][vy] and color[vx][vy] == 0:
                    call(vx, vy)

        
        for i in range(r):
            if color[i][0] == 0 and grid[i][0]:
                call(i, 0)
            if color[i][c-1] == 0 and grid[i][c-1]:
                call(i, c-1)
        
        for i in range(c):
            if color[0][i] == 0 and grid[0][i]:
                call(0, i)
            if color[r-1][i] == 0 and grid[r-1][i]:
                call(r-1, i)
        
        res = 0
        for i in range(r):
            for j in range(c):
                if color[i][j] == 0 and grid[i][j] == 1:
                    res += 1

        return res