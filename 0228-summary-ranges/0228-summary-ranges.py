class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = [[nums[0], nums[0]]]
        for v in nums[1:]:
            if v == res[-1][1] + 1:
                res[-1][1] = v
            else:
                res.append([v, v])
        
        ret = []
        for u, v in res:
            if u == v:
                ret.append(str(v))
            else:
                ret.append(f"{u}->{v}")
        
        return ret