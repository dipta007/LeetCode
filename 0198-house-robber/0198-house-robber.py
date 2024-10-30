class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def call(i, taken):
            if i == len(nums):
                return 0
            
            o1, o2 = -100, -100
            if taken:
                o1 = call(i+1, False)
            else:
                o1 = call(i+1, False)
                o2 = nums[i] + call(i+1, True)
            
            return max(o1, o2)
        
        return call(0, False)