class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def call(a, b):
            if a <= 0 and b > 0:
                return 1.0
            if a <= 0 and b <= 0:
                return 0.5
            if a > 0 and b <= 0:
                return 0.0
            
            res = 0.0
            for aa, bb in [
                [100, 0],
                [75, 25],
                [50, 50],
                [25, 75]
            ]:
                aa = aa // 25
                bb = bb // 25
                res += 0.25 * call(a-aa, b-bb)
            
            return res

        # for i in range(400):
        #     print(i, call(i, i))
        # print(call(10000000, 10000000))
        n = (n // 25) + int(n % 25 != 0)
        # print(call(400, 400))
        if n > 400:
            n = 400
        return call(n, n)
