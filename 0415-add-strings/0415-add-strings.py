class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1 = "0" * (len(num2) - len(num1)) + num1
        else:
            num2 = "0" * (len(num1) - len(num2)) + num2
        
        res = []
        c = 0
        for a, b in zip(num1[::-1], num2[::-1]):
            a = int(a)
            b = int(b)
            c = a + b + c
            res.append(str(c % 10))
            c = c // 10
        
        if c:
            res.append(str(c))
        
        res.reverse()
        return "".join(res)