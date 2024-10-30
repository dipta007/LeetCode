class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r, c = len(mat), len(mat[0])

        res = []
        ind = 0
        for i in range(r):
            rr, cc = i, 0
            curr = []
            while rr >= 0 and cc < c:
                curr.append(mat[rr][cc])
                rr -= 1
                cc += 1
            if ind % 2 == 1:
                curr.reverse()
            res.extend(curr)
            ind += 1
        
        for i in range(1, c):
            rr, cc = r-1, i
            curr = []
            while cc < c and rr >= 0:
                curr.append(mat[rr][cc])
                rr -= 1
                cc += 1
            if ind % 2 == 1:
                curr.reverse()
            res.extend(curr)
            ind += 1
        

        return res