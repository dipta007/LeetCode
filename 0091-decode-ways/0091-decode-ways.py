class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def call(i, curr):
            if curr[0] == '0' or int(curr) > 26:
                return 0
            if i == len(s):
                return 1

            res = call(i+1, curr + s[i])
            res += call(i+1, s[i])

            return res
            
        return call(1, s[0])
