class Solution:
    def minSwaps(self, data: List[int]) -> int:
        tot = sum(data)

        cum = [0]
        for v in data:
            cum.append(cum[-1] + v)
        
        res = 10000000000000
        for i in range(1, len(cum)-tot+1):
            now = cum[i+tot-1] - cum[i-1]
            res = min(res, tot - now)
        return res