class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        mx = 0
        sm = 0
        for v in nums:
            sm += v
            if sm < 0:
                sm = 0
            
            mx = max(mx, sm)

        return mx