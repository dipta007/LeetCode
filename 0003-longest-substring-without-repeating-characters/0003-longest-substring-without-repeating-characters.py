class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        res = 0
        l = 0
        for h in range(len(s)):
            c = s[h]
            count[c] = count.get(c, 0) + 1

            while count[c] > 1:
                lc = s[l]
                count[lc] -= 1
                l += 1

            res = max(res, h - l + 1)

        return res
