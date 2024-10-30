class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        h = []

        intervals.sort(key=lambda x: x[0])

        res = 0
        for x, y in intervals:
            if len(h) == 0:
                heapq.heappush(h, y)
            elif x < h[0]:
                heapq.heappush(h, y)
            elif x >= h[0]:
                heapq.heappop(h)
                heapq.heappush(h, y)
            print(h)
            res = max(res, len(h))
        return res