dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        vis = [[0] * c for _ in range(r)]
        
        def call(ux, uy):
            vis[ux][uy] = 1
            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy
                if vx >= 0 and vy >= 0 and vx < r and vy < c and vis[vx][vy] == 0 and grid[vx][vy] == "1":
                    call(vx, vy)
        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    res += 1
                    call(i, j)
        
        return res
