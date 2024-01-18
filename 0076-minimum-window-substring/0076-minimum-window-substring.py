class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        mp = Counter(t)
        res = ""
        l = 0
        uni = 0
        cnt = defaultdict(int)
        for h in range(len(s)):
            cnt[s[h]] += 1
            while l < len(s) and cnt[s[l]] > mp[s[l]]:
                cnt[s[l]] -= 1
                l += 1

            flg = 1
            for k in mp.keys():
                if mp[k] > cnt[k]:
                    flg = 0
                    break
            # print(mp)
            # print(cnt)
            # print(l, h, flg)
            if flg and (len(res) == 0 or (h-l+1) < len(res)):
                res = s[l:h+1]
        
        return res

