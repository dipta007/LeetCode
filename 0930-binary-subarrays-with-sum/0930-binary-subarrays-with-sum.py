class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)

        count[0] = 1
        cum = 0
        cnt = 0
        for v in nums:
            cum += v
            cnt += count[cum - goal]

            count[cum] += 1

        return cnt

# 1 0 1 0 1
# 1 1 2 2 3
# 1 1 0 0 1

# 1 1 2 2 1
# 0 1 0 1 2