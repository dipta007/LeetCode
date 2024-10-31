class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        cnt = 0
        for x, y in intervals[1:]:
            if x < end:
                cnt += 1
            else:
                end = y

        return cnt