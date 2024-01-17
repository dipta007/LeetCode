class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for v in nums:
            s ^= v
        return s