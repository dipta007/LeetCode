class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import defaultdict

        res = 0
        for i in range(1, 27):
            uniq = 0
            cnt = defaultdict(int)
            satisfyc = 0

            l = 0
            for h in range(len(s)):
                hc = s[h]

                if cnt[hc] == 0:
                    uniq += 1
                cnt[hc] += 1

                if cnt[hc] == k:
                    satisfyc += 1

                while uniq > i:
                    lc = s[l]
                    cnt[lc] -= 1

                    if cnt[lc] == 0:
                        uniq -= 1

                    if cnt[lc] == k-1:
                        satisfyc -= 1
                    
                    l += 1
            
                if satisfyc == uniq:
                    res = max(res, h - l + 1)

        return res
                    