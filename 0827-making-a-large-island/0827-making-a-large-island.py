dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        color = [[0] * n for _ in range(n)]
        c = 1
        area = {}

        def call(ux, uy, clr):
            color[ux][uy] = clr

            a = 1
            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < n and vy < n and color[vx][vy] == 0 and grid[vx][vy] == 1:
                    a += call(vx, vy, clr)
            return a
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] and color[i][j] == 0:
                    a = call(i, j, c)
                    area[c] = a
                    c += 1
            
        res = max(area.values()) if len(area) > 0 else 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    s = set()
                    for dxx, dyy in zip(dx, dy):
                        vx = x + dxx
                        vy = y + dyy
                        if vx >= 0 and vy >= 0 and vx < n and vy < n and grid[vx][vy] == 1:
                            s.add(color[vx][vy])
                    
                    # print(x, y, s)
                    a = 0
                    for c in s:
                        a += area[c]

                    res = max(res, a + 1)

        return res                

