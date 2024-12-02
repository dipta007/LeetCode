class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr = -1
        for v in prices:
            if curr == -1:
                curr = v
            elif v > curr:
                res += (v - curr)
                curr = v
            else:
                curr = v
        return res