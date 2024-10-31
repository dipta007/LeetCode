class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        def call(lx, ly, rx, ry):
            if lx > rx or ly > ry:
                return
            
            for i in range(ly, ry+1):
                res.append(mat[lx][i])

            for i in range(lx+1, rx+1):
                res.append(mat[i][ry])

            if lx < rx and ly < ry:
                for i in range(ry-1, ly-1, -1):
                    res.append(mat[rx][i])

                for i in range(rx-1, lx, -1):
                    res.append(mat[i][ly])
            
            call(lx + 1, ly + 1, rx - 1, ry - 1)

        call(0, 0, len(mat)-1, len(mat[0])-1)

        return res