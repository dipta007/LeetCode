class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0: return True
        intervals.sort(key=lambda x: x[0])

        last = intervals[0][1]
        for i in range(1, len(intervals)):
            x, y = intervals[i]

            if x < last:
                return False

            last = y
        
        return True