class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot_ind = 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= nums[-1]:
                r = m - 1
                pivot_ind = m
            else:
                l = m + 1
        

        return nums[pivot_ind]