class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def call(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            
            res = 0
            if s[i] == s[j]:
                res = max(res, 2 + call(i+1, j-1))
            
            res = max(res, call(i+1, j))
            res = max(res, call(i, j-1))

            return res
        
        kk = len(s) - call(0, len(s) - 1)
        return kk <= k