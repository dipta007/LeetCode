class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        res = 0
        l = 0
        cum = 0
        for r in range(len(nums)):
            v = nums[r]
            count[v] += 1
            cum += v

            while count[v] > 1:
                count[nums[l]] -= 1
                cum -= nums[l]
                l += 1
            
            res = max(res, cum)
        return res