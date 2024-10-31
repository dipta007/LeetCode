class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(s)
        s = [int(x) for x in s]

        @cache
        def call(i, curr):
            if curr == 0 or curr > 26:
                return 0
            if i == len(s):
                return 1

            res = call(i+1, curr * 10 + s[i])
            res += call(i+1, s[i])

            return res
            
        return call(1, s[0])
