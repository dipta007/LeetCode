dx = [-1, -1, -2, -2, 1, 1, 2, 2]
dy = [-2, 2, -1, 1, -2, 2, -1, 1]
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        from collections import deque
        
        vis = {}
        for i in range(-300, 301):
            vis[i] = {}
            for j in range(-300, 301):
                vis[i][j] = 0

        def bfs(ux, uy):
            q = deque()
            q.append((ux, uy, 0))

            while len(q):
                ux, uy, d = q.popleft()
                if ux == x and uy == y:
                    return d
                for dxx, dyy in zip(dx, dy):
                    vx = ux + dxx
                    vy = uy + dyy

                    if vx >= -300 and vy >= -300 and vx <= 300 and vy <= 300 and vis[vx][vy] == 0:
                        vis[vx][vy] = 1
                        q.append((vx, vy, d+1))
                
        return bfs(0, 0)

        