class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums + [float("-inf")]
        def call(l, r):
            m = (l + r ) // 2

            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m
            
            if nums[m+1] > nums[m]:
                return call(m+1, r)
            
            if nums[m-1] > nums[m]:
                return call(l, m-1)

        return call(1, len(nums)-1) - 1