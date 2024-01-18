class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        mn = 1000000000
        ind = 0

        rgt = sum(nums)
        lft = 0
        for i in range(len(nums)):
            v = nums[i]
            lft += v
            rgt -= v

            lft_avg = lft // (i+1)
            rgt_avg = rgt // ((len(nums) - i - 1) if i < len(nums)-1 else 1)
            nw = abs(lft_avg - rgt_avg)

            if nw < mn:
                mn = nw
                ind = i

        return ind