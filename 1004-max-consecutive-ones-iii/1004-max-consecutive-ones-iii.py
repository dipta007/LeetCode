class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        remaining = k
        res = 0
        for h in range(len(nums)):
            if nums[h] == 0:
                while remaining == 0 and l < h:
                    remaining += int(nums[l] == 0)
                    l += 1
                
                if remaining:
                    remaining -= 1
                else:
                    l += 1
            
            res = max(res, h - l + 1)

        return res
            

            
