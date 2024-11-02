class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0" * (len(b) - len(a)) + a
        b = "0" * (len(a) - len(b)) + b

        a = [int(x) for x in list(a)]
        b = [int(x) for x in list(b)]
        
        a.reverse()
        b.reverse()

        def add(a, b):
            if a > b: a, b = b, a
            if a == 1 and b == 1:
                return 10
            if a == 0 and b == 1:
                return 1
            return a + b

        res = []
        c = 0
        
        for aa, bb in zip(a, b):
            c = add(c, add(aa, bb))
            # print(aa, bb, c, c//10, c%10)
            res.append(c % 10)
            c //= 10
        
        if c: res.append(c)

        res.reverse()

        return "".join(str(x) for x in res)