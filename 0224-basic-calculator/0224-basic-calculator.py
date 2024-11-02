class Solution:
    def calculate(self, s: str) -> int:
        def get_num(ind):
            num = 0
            for i in range(ind, len(s)):
                if s[i].isnumeric():
                    num = num * 10 + int(s[i])
                else:
                    return num, i
            return num, i

        def calc(stack):
            curr = []
            while True:
                sc = stack.pop()
                if sc == '(':
                    break
                curr.append(sc)
            curr.reverse()
            cum = curr[0]
            i = 1
            while i < len(curr):
                if curr[i] == '+':
                    cum = cum + curr[i+1]
                    i = i + 2
                elif curr[i] == '-':
                    cum = cum - curr[i+1]
                    i = i + 2
            return cum

        stack = []
        i = 0
        s = '(' + s + ')'
        while i < len(s):
            # print(i)
            c = s[i]

            if c == '(':
                stack.append('(')
                i += 1
            elif c == ')':
                # calc
                num = calc(stack)
                stack.append(num)
                i += 1
            elif c == '-':
                if len(s) == 0 or not isinstance(stack[-1], int):
                    stack.append(0)
                    stack.append('-')
                    i += 1
                else:
                    stack.append('-')
                    i += 1
            elif c == '+':
                stack.append('+')
                i += 1
            elif c.isnumeric():
                num, i = get_num(i)
                stack.append(num)
            else: 
                i += 1

            # print(i, stack)
        
        return stack[-1]