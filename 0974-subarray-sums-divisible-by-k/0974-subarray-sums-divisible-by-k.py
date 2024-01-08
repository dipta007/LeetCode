class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        nums = [x%k for x in nums]
        from collections import defaultdict
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        cum = 0
        for v in nums:
            cum += v
            cum %= k
            res += mp[cum]
            mp[cum] += 1
        return res