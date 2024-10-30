class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        res = 0
        for i in range(1, len(prices)):
            v = prices[i]
            res = max(res, v - mn)
            mn = min(mn, v)
        
        return res