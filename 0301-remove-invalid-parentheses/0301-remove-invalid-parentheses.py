class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        p = 0
        rmv = 0
        for c in s:
            if c == '(':
                p += 1
            if c == ')':
                p -= 1

            if p < 0:
                rmv += abs(p)
                p = 0
            
        if p:
            rmv += abs(p)
        
        res = []
        def call(i, p, rmvd, curr):
            if p < 0:
                return
            if rmvd < 0:
                return
            
            if i == len(s):
                if p == 0 and rmvd == 0:
                    nonlocal res
                    res.append(curr[:])
                return

            if s[i] in ['(', ')']:
                call(i+1, p, rmvd-1, curr) # maybe remove?

                pp = p 
                if s[i] == '(': pp += 1
                elif s[i] == ')': pp -= 1
                call(i+1, pp, rmvd, curr + s[i]) # keep it
            else:
                call(i+1, p, rmvd, curr + s[i])

            
        call(0, 0, rmv, "")
        return list(set(res))