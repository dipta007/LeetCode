class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        res = 0
        for v in nums:
            res += (v - mn)
        
        return res