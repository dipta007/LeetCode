class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(mxw):
            d = 0
            cum = 0
            for w in weights:
                if cum + w > mxw:
                    cum = w
                    d += 1
                else:
                    cum += w
            
            return d + 1 if cum else d

        
        l, h = max(weights), sum(weights)
        res = -1
        while l <= h:
            m = (l + h) // 2
            if check(m) <= days:
                h = m - 1
                res = m
            else:
                l = m + 1

        return res