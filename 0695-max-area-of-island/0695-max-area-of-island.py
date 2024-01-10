dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        color = [[0 for _ in range(c)] for _ in range(r)]

        def call(x, y):
            color[x][y] = 1

            res = 1
            for dxx, dyy in zip(dx, dy):
                vx = x + dxx
                vy = y + dyy

                if vx < 0 or vx >= r or vy < 0 or vy >= c:
                    continue

                if color[vx][vy] == 0 and grid[vx][vy] == 1:
                    res += call(vx, vy)

            return res

        res = 0
        for i in range(r):
            for j in range(c):
                if color[i][j] == 0 and grid[i][j] == 1:
                    res = max(res, call(i, j))

        return res