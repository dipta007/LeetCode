class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(nums)):
            v = nums[r]
            count[v] += 1

            while count[v] > 1:
                count[nums[l]] -= 1
                l += 1
            
            res = max(res, sum(nums[l:r+1]))
        return res