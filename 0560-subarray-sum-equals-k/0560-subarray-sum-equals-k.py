class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if k == 0 and len(nums) == 0:
            return 1
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1

        cum = 0
        res = 0
        for v in nums:
            cum += v
            res += count[cum - k]
            count[cum] += 1

        return res

