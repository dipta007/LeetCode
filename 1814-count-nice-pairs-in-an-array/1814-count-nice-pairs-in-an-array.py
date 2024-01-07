class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])

        def nCr(n, r):
            res = n * (n-1)
            res //= 2
            res %= int(1e9+7)
            return res
        
        from collections import defaultdict
        mp = defaultdict(int)
        for v in nums:
            mp[(v - rev(v))] += 1
        
        res = 0
        for k, v in mp.items():
            if v >= 2:
                res += nCr(v, 2)
                res %= int(1e9+7)
        return res