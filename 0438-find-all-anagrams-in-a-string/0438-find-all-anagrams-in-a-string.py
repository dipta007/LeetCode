class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        from collections import defaultdict
        cp = defaultdict(int)
        cnt_p = 0
        for c in p:
            if cp[c] == 0:
                cnt_p += 1
            cp[c] += 1
        
        from collections import deque
        dq = deque()

        l = 0
        cnt_s = 0
        sp = defaultdict(int)
        res = []
        for h in range(len(s)):
            hc = s[h]
            sp[hc] += 1
            if sp[hc] == cp[hc]:
                cnt_s += 1

            if h >= len(p):
                pc = s[l]
                if sp[pc] == cp[pc]:
                    cnt_s -= 1
                sp[pc] -= 1
                l += 1
            
            # print(h, sp, cnt_s, cnt_p)
            if cnt_s == cnt_p:
                res.append(l)

        return res