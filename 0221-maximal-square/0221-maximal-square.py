class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        mat = [[int(c) for c in col] for col in mat]

        r, c = len(mat), len(mat[0])
        for i in range(r):
            for j in range(c):
                curr = mat[i][j]
                if i > 0:
                    curr += mat[i-1][j]
                if j > 0:
                    curr += mat[i][j-1]
                if i > 0 and j > 0:
                    curr -= mat[i-1][j-1]

                mat[i][j] = curr
        
        def get(lx, ly, rx, ry):
            curr = mat[rx][ry]
            if lx > 0:
                curr -= mat[lx-1][ry]
            if ly > 0:
                curr -= mat[rx][ly-1]
            if lx > 0 and ly > 0:
                curr += mat[lx-1][ly-1]
            return curr

        res = 0
        for lx in range(r):
            for ly in range(c):
                for k in range(min(r-lx, c-ly), res, -1):
                    rx, ry = lx + k - 1, ly + k - 1

                    if get(lx, ly, rx, ry) == k*k:
                        res = max(res, k)
                        break

        return res*res