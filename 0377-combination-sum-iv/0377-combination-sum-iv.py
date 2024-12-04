class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def call(curr):
            if curr < 0:
                return 0
            if curr == 0:
                return 1
            
            res = 0
            for v in nums:
                res += call(curr - v)
            
            return res
        
        return call(target)