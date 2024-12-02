class Solution:
    def maxEqualRowsAfterFlips(self, m: List[List[int]]) -> int:
        r, c = len(m), len(m[0])

        o1s, o2s = [], []
        for i in range(r):
            o1, o2 = "", ""

            for j in range(c):
                o1 += ("0" if m[i][j] == 0 else "1")
                o2 += ("1" if m[i][j] == 0 else "0")
            
            o1s.append(o1)
            o2s.append(o2)
        
        res = 0
        for i in range(r):
            cnt = 0
            for j in range(r):
                if o1s[j] == o1s[i] or o2s[j] == o1s[i] or o1s[j] == o2s[i] or o2s[j] == o2s[i]:
                    cnt += 1
            
            res = max(res, cnt)

        return res