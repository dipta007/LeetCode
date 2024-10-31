dp = None

class Solution:
    def longestPalindrome(self, s: str) -> str:
        global dp
        dp = [[-1] * len(s) for _ in range(len(s))]
        def call(i, j):
            if i >= j:
                return True
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = call(i+1, j-1)
            else:
                dp[i][j] = False
                
            return dp[i][j]

        x, y = -1, -1
        mx = 0
        for i in range(len(s)):
            for j in range(len(s)-1, i-1, -1):
                if j - i + 1 < mx: continue
                if call(i, j):
                    if j - i + 1 > mx:
                        mx = j - i + 1
                        x, y = i, j
        return s[x:y+1]