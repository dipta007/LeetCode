class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mark = [0] * len(nums)

        res = []
        def call(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            
            call(i+1, curr + [nums[i]])
            call(i+1, curr)
        
        call(0, [])
        return res