dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = [[0 for _ in range(c)] for __ in range(r)]
        def dfs(ux, uy):
            visited[ux][uy] = 1

            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy
                if vx >= 0 and vy >= 0 and vx < r and vy < c and visited[vx][vy] == 0 and grid[vx][vy] == '1':
                    dfs(vx, vy)
        
        cnt = 0
        for i in range(r):
            for j in range(c):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt
