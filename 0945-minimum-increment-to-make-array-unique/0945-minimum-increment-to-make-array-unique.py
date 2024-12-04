class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        low = nums[0]
        res = 0
        for v in nums:
            if v >= low:
                low = v + 1
            else:
                res += (low - v)
                low += 1

        return res