class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def call(i, j):
            if i == len(s):
                while j < len(p) and p[j] == '*': j += 1
                while j < len(p) and j + 1 < len(p) and p[j+1] == '*':
                    j = j + 2
                print(i, j)
                return j == len(p)
            if j == len(p):
                return False

            res = False
            if s[i] == p[j] or p[j] == '.':
                res = res or call(i+1, j+1)
            if p[j] == '*':
                if s[i] == p[j-1] or p[j-1] == '.':
                    res = res or call(i+1, j)
                    res = res or call(i+1, j+1)
                res = res or call(i, j+1)

            if j+1 < len(p) and p[j+1] == '*':
                res = res or call(i, j+2)
            return res
        
        return call(0, 0)