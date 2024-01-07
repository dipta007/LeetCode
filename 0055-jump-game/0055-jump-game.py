class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        last = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            mx_ind = i + nums[i]
            if mx_ind >= last:
                dp[i] = True
                last = i
        
        return dp[0]