dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        @cache
        def call(ux, uy):
            cval = matrix[ux][uy]

            res = 0
            for dxx, dyy in zip(dx, dy):
                vx = ux + dxx
                vy = uy + dyy

                if vx >= 0 and vy >= 0 and vx < r and vy < c:
                    if matrix[vx][vy] > cval:
                        res = max(res, call(vx, vy))

            return res + 1

        res = 1
        for i in range(r):
            for j in range(c):
                res = max(res, call(i, j))

        return res