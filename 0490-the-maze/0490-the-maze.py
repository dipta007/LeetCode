dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        from collections import deque
        dq = deque()

        r, c = len(maze), len(maze[0])

        dmaze = [[1] * (c+2) for _ in range(r+2)]
        for i in range(r):
            for j in range(c):
                dmaze[i+1][j+1] = maze[i][j]

        start = [start[0] + 1, start[1] + 1]
        destination = [destination[0] + 1, destination[1] + 1]

        r, c = len(dmaze), len(dmaze[0])

        dq.append(start)

        vis = [[0] * c for _ in range(r)]
        vis[start[0]][start[1]] = 1

        while len(dq) > 0:
            ux, uy = dq.popleft()

            if ux == destination[0] and uy == destination[1]:
                return True

            for dxx, dyy in zip(dx, dy):
                vx, vy = ux + dxx, uy + dyy

                while vx < r and vy < c and vx >= 0 and vy >= 0 and dmaze[vx][vy] == 0:
                    vx = vx + dxx
                    vy = vy + dyy
                
                vx = vx - dxx
                vy = vy - dyy
            
                if vis[vx][vy] == 0:
                    dq.append([vx, vy])
                    vis[vx][vy] = 1
                

        return False