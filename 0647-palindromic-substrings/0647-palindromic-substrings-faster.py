class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def check(i, j):
            if i >= j:
                return True

            if s[i] == s[j]:
                return check(i+1, j-1)
            return False

        @cache
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            l += 1
            r -= 1
            return r - l + 1

        cnt = 0
        for i in range(len(s)):
            # odd
            odd_len = expand(i, i)
            cnt += (odd_len // 2 + 1)

            # even
            if i+1 < len(s) and s[i] == s[i+1]:
                even_len = expand(i, i+1)
                cnt += (even_len // 2)
        
        return cnt