class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev, cur = 0, 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        ans += min(prev, cur)
        return ans
            
        