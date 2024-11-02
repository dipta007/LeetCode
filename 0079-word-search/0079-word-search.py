dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        vis = [[0] * c for _ in range(r)]

        def call(i, ux, uy, color):
            if i == len(word) - 1:
                return True
            vis[ux][uy] = color

            res = False
            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < r and vy < c and vis[vx][vy] < color and board[vx][vy] == word[i+1]:
                    res = res or call(i+1, vx, vy, color)

            vis[ux][uy] = 0
            return res

        clr = 1
        res = False
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    res = res or call(0, i, j, clr)
                    clr += 1
        
        return res