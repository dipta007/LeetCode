class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rgt = 0
        for i in range(len(s)-1, -1, -1):
            rgt += int(s[i] == ')')

        res = ""
        lft = 0
        for i, c in enumerate(s):
            if s[i] == '(' and rgt:
                res += s[i]
                lft += 1
                rgt -= 1
            elif s[i] == ')':
                if lft:
                    lft -= 1
                    res += s[i]
                else: rgt -= 1
            elif s[i] not in ['(', ')']:
                res += s[i]
    
        return res