class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1:
            return False

        @cache
        def call(i, tot):
            if tot < 0:
                return False
            if i == len(nums):
                return tot == 0
            
            return call(i+1, tot) or call(i+1, tot-nums[i])
        
        return call(0, tot // 2)