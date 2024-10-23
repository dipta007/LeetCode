class Solution:
    def validPalindrome(self, s: str) -> bool:
        @cache
        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def call(i, used):
            j = len(s) - i - 1
            if i >= j:
                return True
            
            if s[i] == s[j]:
                return call(i+1, used)
            elif not used:
                return check(i+1, j) or check(i, j-1)
            return False
        
        return call(0, 0)