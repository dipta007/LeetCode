class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == '(' and c != ')':
                    return False
                if stack[-1] == '{' and c != '}':
                    return False
                if stack[-1] == '[' and c != ']':
                    return False
                stack.pop()

        return not stack