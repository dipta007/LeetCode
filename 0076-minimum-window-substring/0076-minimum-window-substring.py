class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcounter = {}
        tcnt = 0
        for c in t:
            tcounter[c] = tcounter.get(c, 0) + 1
        tcnt = len(tcounter)

        scounter = {}
        l = 0
        scnt = 0
        res = len(s) + 10
        ret = ""
        for h in range(len(s)):
            c = s[h]
            scounter[c] = scounter.get(c, 0) + 1
            if scounter[c] == tcounter.get(c, 0):
                scnt += 1
            while scnt == tcnt:
                # print(h, scnt, tcnt, l, scounter)
                if h - l + 1 < res:
                    ret = s[l:h+1]
                    res = h - l + 1
                lc = s[l]
                scounter[lc] -= 1
                l += 1
                if scounter[lc] < tcounter.get(lc, 0):
                    scnt -= 1
            
        return ret