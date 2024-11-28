class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        tot = 0
        res = float('inf')
        for h in range(len(nums)):
            v = nums[h]
            tot += v

            while tot >= target:
                res = min(res, h - l + 1)
                tot -= nums[l]
                l += 1
        
        return res if res < float('inf') else 0