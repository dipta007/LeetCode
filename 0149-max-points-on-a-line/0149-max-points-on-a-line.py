class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get(u, l):
            neg = 0
            if u * l < 0:
                neg = 1
            
            u = abs(u)
            l = abs(l)

            gc = gcd(u, l)
            if gc == 0: gc = 1
            u //= gc
            l //= gc

            if neg: u = -u
            return (u, l)
        
        res = 1
        from collections import defaultdict
        for i, p1 in enumerate(points):
            count = defaultdict(int)
            for p2 in points:
                if p1 == p2: 
                    continue
                u = p2[1] - p1[1]
                l = p2[0] - p1[0]
                ul = get(u, l)

                count[ul] += 1
            
            if len(count) > 0:
                res = max(res, max(count.values()) + 1)
        
        return res