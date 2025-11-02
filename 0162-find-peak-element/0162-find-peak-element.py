class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [min(nums)-1] + nums + [min(nums)-1]
        l, h = 1, len(nums) - 2
        while l <= h:
            m = (l + h) // 2
            if nums[m-1] < nums[m] and nums[m+1] < nums[m]:
                return m-1
            
            if nums[m-1] > nums[m]:
                h = m-1
            else:
                l = m+1
        
        