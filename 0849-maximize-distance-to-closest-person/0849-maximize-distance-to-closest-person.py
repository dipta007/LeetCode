class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = -1
        res = -1
        for i, v in enumerate(seats):
            if v:
                if prev == -1:
                    res = i
                else:
                    nw = (i - prev - 1) // 2 + int((i - prev - 1) % 2 != 0)
                    res = max(res, nw)
                prev = i
        
        res = max(res, len(seats) - prev - 1)
        return res
            