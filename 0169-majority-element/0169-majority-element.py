class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bit = 1
        res = 0
        for i in range(1, 64):
            tot = 0
            for v in nums:
                tot += (1 if (abs(v) & bit) else -1)
            
            if tot > 0:
                res = (res | bit)

            bit = bit << 1
        
        neg = sum(1 if v < 0 else -1 for v in nums)
        if neg > 0:
            res *= -1
        
        return res
            
