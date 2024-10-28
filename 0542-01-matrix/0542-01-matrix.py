dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque

        r, c = len(mat), len(mat[0])

        q = deque()
        vis = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i, j))
                    vis[i][j] = 0
                else:
                    vis[i][j] = float('inf')
        

        while len(q) > 0:
            ux, uy = q.popleft()

            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < r and vy < c and vis[vx][vy] == float('inf'):
                    vis[vx][vy] = vis[ux][uy] + 1
                    q.append((vx, vy))

        return vis