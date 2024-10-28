class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        val = 1
        def call(lx, ly, rx, ry):
            nonlocal val
            for i in range(ly, ry+1):
                mat[lx][i] = val
                val += 1

            for i in range(lx+1, rx+1):
                mat[i][ry] = val
                val += 1
            
            for i in range(ry-1, ly-1, -1):
                mat[rx][i] = val
                val += 1

            for i in range(rx-1, lx, -1):
                mat[i][ly] = val
                val += 1
        
        lx, ly, rx, ry = 0, 0, n-1, n-1
        while lx <= rx and ly <= ry:
            call(lx, ly, rx, ry)
            # print(mat)
            lx += 1
            ly += 1
            rx -= 1
            ry -= 1
        
        return mat