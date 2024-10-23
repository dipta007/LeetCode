class Solution:
    def calculate(self, s: str) -> int:
        fs = [c for c in s if c != ' ']

        def get(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a // b

        res = []
        num = 0
        strt = False
        for c in fs:
            if c.isnumeric():
                num = num * 10 + int(c)
                strt = True
            else:
                if strt:
                    res.append(num)
                    num = 0
                    strt = False
                    res.append(c)
        if strt:
            res.append(num)
        
        fres = []
        i = 0
        while i < len(res):
            v = res[i]
            if v == '*' or v == '/':
                a = fres.pop()
                op = v
                b = res[i+1]
                fres.append(get(a, b, op))
                i += 1
            else:
                fres.append(v)
            i += 1
        
        cum = 0
        op = ''
        for v in fres:
            if v == '+' or v == '-':
                op = v
            else:
                if op:
                    cum = get(cum, v, op)
                else:
                    cum = v
        return cum