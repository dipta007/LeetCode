class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if len(stack):
                    stack.pop()
                else:
                    res += 1
        
        res += len(stack)
        return res