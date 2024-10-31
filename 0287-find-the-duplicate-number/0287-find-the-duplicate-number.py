class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, h = 1, len(nums)
        res = -1
        while l < h:
            m = (l + h) // 2

            cnt = 0
            for v in nums:
                if v <= m:
                    cnt += 1
            
            if cnt > m:
                res = m
                h = m
            else:
                l = m + 1
        
        return res