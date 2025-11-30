class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        q = []

        intervals.sort(key=lambda x: x[0])
        heapq.heappush(q, intervals[0][1])

        res = 1
        for [s, e] in intervals[1:]:
            if s >= q[0]:
                heapq.heappop(q)
            heapq.heappush(q, e)
            res = max(res, len(q))
        
        return res

        