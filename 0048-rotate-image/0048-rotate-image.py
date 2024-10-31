class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rot(lx, ly, rx, ry):
            if lx >= rx:
                return
            # n = rx - lx

            tmp = mat[lx][ly:ry+1]
            # print(tmp)
            c = ry
            for r in range(lx, rx+1, 1):
                mat[lx][c] = mat[r][ly]
                c -= 1
            
            r = lx
            for c in range(ly, ry+1, 1):
                mat[r][ly] = mat[rx][c]
                r += 1

            c = ly
            for r in range(rx, lx-1, -1):
                mat[rx][c] = mat[r][ry]
                c += 1

            i = 0
            for r in range(lx, rx+1, 1):
                mat[r][ry] = tmp[i]
                i += 1


            rot(lx+1, ly+1, rx-1, ry-1)
            
        rot(0, 0, len(mat)-1, len(mat)-1)



