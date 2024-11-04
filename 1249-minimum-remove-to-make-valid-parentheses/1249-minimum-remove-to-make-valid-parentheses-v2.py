class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # rgt = 0
        # for i in range(len(s)-1, -1, -1):
        #     rgt += int(s[i] == ')')

        # res = ""
        # lft = 0
        # for i, c in enumerate(s):
        #     if s[i] == '(' and rgt:
        #         res += s[i]
        #         lft += 1
        #         rgt -= 1
        #     elif s[i] == ')':
        #         if lft:
        #             lft -= 1
        #             res += s[i]
        #         else: rgt -= 1
        #     elif s[i] not in ['(', ')']:
        #         res += s[i]
    
        # return res

        p = 0
        cnt = 0
        left_indices = []
        rmv = set()
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                p += 1
                left_indices.append(i)
            elif c == ')':
                p -= 1
                if p < 0:
                    cnt += 1
                    p = 0
                    rmv.add(i)
            else:
                continue

        if p:
            for ind in left_indices[-p:]:
                rmv.add(ind)
            
        res = ""
        for i in range(len(s)):
            c = s[i]
            if i not in rmv:
                res += c

        return res