class Solution:
    def myAtoi(self, s: str) -> int:
        neg, start = False, False
        s = s.strip()
        if len(s) == 0: return 0
        if s[0] == '-':
            neg = True
        if s[0] in '+-':
            s = s[1:]
        
        res = 0
        for c in s:
            if c.isnumeric():
                print(c)
                start = True
                res = res * 10 + int(c)
            else:
                break
        
        res = res if neg == False else -res
        if res < -2147483648:
            res = -2147483648
        if res > 2147483647:
            res = 2147483647
        return res