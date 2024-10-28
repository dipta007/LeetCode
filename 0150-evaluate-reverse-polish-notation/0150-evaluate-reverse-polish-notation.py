class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def get(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/':
                aa = abs(a)
                bb = abs(b)
                if a * b < 0: return - (aa // bb)
                else: return aa // bb
        
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                stack.append(get(a, b, t))
            else:
                stack.append(int(t))
        
        return stack[-1]
