from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0: return -1
        r, c = len(grid), len(grid[0])
        q = deque()
        q.append((0, 0, 1))

        vis = [[0] * c for _ in range(r)]
        while len(q):
            ux, uy, d = q.popleft()
            if ux == r-1 and uy == c-1:
                return d

            for dxx, dyy in zip(dx, dy):
                vx, vy = ux + dxx, uy + dyy

                if vx >= 0 and vy >= 0 and vx < r and vy < c and grid[vx][vy] == 0:
                    if vis[vx][vy] == 0:
                        q.append((vx, vy, d+1))
                        vis[vx][vy] = 1
        return -1
