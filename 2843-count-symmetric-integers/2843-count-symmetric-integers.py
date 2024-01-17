class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check(x):
            x = str(x)
            if len(x) % 2 == 1: return 0
            sm = 0
            for i in range(len(x)):
                if i < len(x) // 2:
                    sm += int(x[i])
                else:
                    sm -= int(x[i])
            return sm == 0
        
        return sum([check(x) for x in range(low, high+1)])
        
