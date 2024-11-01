dx = [-2, -1, 2, 1, 2, 1, -2, -1]
dy = [-1, -2, -1, -2, 1, 2, 1, 2]

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        from collections import deque
        vis = {}
        dq = deque()

        dq.append((0, 0, 0))
        while len(dq):
            ux, uy, d = dq.popleft()

            if ux == x and uy == y:
                return d

            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= -300 and vy >= -300 and vx <= 300 and vy <= 300 and (vx, vy) not in vis:
                    vis[(vx, vy)] = 1
                    dq.append((vx, vy, d+1))
        
