class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        pre_cum = 1
        for v in nums:
            pre_cum *= v
            res = max(res, pre_cum)
            if pre_cum == 0:
                pre_cum = 1
            
        suf_cum = 1
        for v in nums[::-1]:
            suf_cum *= v
            res = max(res, suf_cum)
            if suf_cum == 0:
                suf_cum = 1
            
        return res
            