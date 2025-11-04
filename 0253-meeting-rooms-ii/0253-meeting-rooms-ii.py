class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        h = []
        intervals.sort(key=lambda x: (x[0], x[1]))

        res = 1
        heapq.heappush(h, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] < h[0]:
                heapq.heappush(h, intervals[i][1])
            else:
                heapq.heappop(h)
                heapq.heappush(h, intervals[i][1])
            res = max(res, len(h))
        return res
        