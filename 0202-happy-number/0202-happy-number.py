class Solution:
    def isHappy(self, n: int) -> bool:
        from collections import defaultdict
        mp = defaultdict(int)
        
        while mp[n] == 0:
            mp[n] = 1
            nw = 0
            while n:
                x = n%10
                nw += x*x
                n //= 10
            n = nw
        
        return n == 1