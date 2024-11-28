class Solution:
    def makesquare(self, ms: List[int]) -> bool:
        def turn_on(x, i):
            return x | (1 << i)

        def check(x, i):
            return x & (1 << i)

        def done(x):
            for i in range(len(ms)):
                if not check(x, i):
                    return False
            return True
        
        tot = sum(ms)
        if tot % 4 != 0:
            return False
        
        mid = tot // 4

        @cache
        def call(mask, curr, tot):
            if tot == 4:
                return done(mask)

            if curr == mid:
                return call(mask, 0, tot+1)
            
            if curr > mid:
                return False

            ret = False
            for i in range(len(ms)):
                if check(mask, i) == 0:
                    ret = ret or call(turn_on(mask, i), curr + ms[i], tot)
            
            return ret

        
        return call(0, 0, 0)