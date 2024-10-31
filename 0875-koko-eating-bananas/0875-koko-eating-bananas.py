class Solution:
    def minEatingSpeed(self, piles: List[int], hrs: int) -> int:
        def check(kk):
            hh = 0
            for p in piles:
                hh += int(p / kk) + int(p%kk != 0)
            
            return hh <= hrs
        
        l, h = 1, sum(piles)
        res = 0
        while l <= h:
            m = (l + h) // 2
            if check(m):
                h = m - 1
                res = m
            else:
                l = m + 1
            
        return res