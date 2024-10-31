class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1
        
        res = 0
        odd = 0
        for c, v in cnt.items():
            if v%2 == 1:
                if not odd:
                    res += v
                    odd = 1
                else:
                    res += (v-1)
            else:
                res += v
        return res