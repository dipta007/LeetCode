class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni = []
        done = False
        if len(intervals) == 0 or newInterval[0] <= intervals[0][0]:
            ni.append(newInterval)
            done = True

        for i in range(0, len(intervals)):
            ni.append(intervals[i])

            if not done and newInterval[0] >= intervals[i][0]:
                if i == len(intervals) - 1 or newInterval[0] <= intervals[i+1][0]:
                    ni.append(newInterval)
                    done = True
        # print(ni)
        intervals = [ni[0]]
        for x, y in ni[1:]:
            if x <= intervals[-1][1]:
                intervals[-1][1] = max(intervals[-1][1], y)
            else:
                intervals.append([x, y])

        return intervals