class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        ret = [intervals[0]]
        for [x, y] in intervals[1:]:
            if x <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], y)
            else:
                ret.append([x, y])
        return ret