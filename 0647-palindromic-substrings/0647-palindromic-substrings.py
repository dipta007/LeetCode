class Solution:
    def countSubstrings(self, s: str) -> int:
        @cache
        def check(i, j):
            if i >= j:
                return True

            if s[i] == s[j]:
                return check(i+1, j-1)
            return False

        cnt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j):
                    cnt += 1
        
        return cnt