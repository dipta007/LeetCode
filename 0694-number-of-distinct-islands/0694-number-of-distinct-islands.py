dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = ["U", "D", "L", "R"]

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        vis = [[0] * len(grid[0]) for _ in range(len(grid))]
        island = set()
        currd = ""

        def call(ux, uy, s):
            nonlocal currd
            currd += s
            vis[ux][uy] = 1

            for dxx, dyy, d in zip(dx, dy, dir):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < len(grid) and vy < len(grid[0]) and vis[vx][vy] == 0 and grid[vx][vy]:
                    call(vx, vy, d)
            
            currd += "E"

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j] == 0 and grid[i][j]:
                    cnt += 1
                    currd = ""
                    call(i, j, "S")
                    island.add(currd)

        return len(island)