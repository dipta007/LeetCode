dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        from collections import deque

        r, c = len(grid), len(grid[0])

        dq = deque()
        vis = [[-1 for i in range(c)] for j in range(r)]

        def dfs(ux, uy):
            dq.append((ux, uy))
            vis[ux][uy] = 0

            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < r and vy < c and grid[vx][vy] == 1 and vis[vx][vy] == -1:
                    dfs(vx, vy)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            if len(dq):
                break

        while len(dq) > 0:
            ux, uy = dq.popleft()
            print(ux, uy)
            if grid[ux][uy] and vis[ux][uy] > 0:
                return vis[ux][uy] - 1
            
            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < r and vy < c and vis[vx][vy] == -1:
                    vis[vx][vy] = vis[ux][uy] + 1
                    dq.append((vx, vy))

            