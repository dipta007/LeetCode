class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        import heapq
        h = []

        res = 0
        intervals.sort()
        for x, y in intervals:
            if len(h) == 0 or h[0] >= x:
                heapq.heappush(h, y)
            else:
                mn = heapq.heappop(h)
                heapq.heappush(h, y)
            
            res = max(res, len(h))
        
        return res