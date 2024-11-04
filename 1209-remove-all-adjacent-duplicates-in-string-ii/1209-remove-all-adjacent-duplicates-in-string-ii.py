class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        cnt = 0
        for c in s:
            if stack and c == stack[-1][0]:
                stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, 1))
            
            if stack and stack[-1][1] == k:
                tmp = stack[-1][0]
                while stack and stack[-1][0] == tmp:
                    stack.pop()
        
        return "".join([v[0] for v in stack])
