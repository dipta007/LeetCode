class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        counter = {x: 1 for x in nums}
        for i, n in enumerate(nums):
            cnt = 0
            x = n
            while True:
                if x in counter:
                    x = x * x
                    cnt += 1
                else: break
            res = max(res, cnt)
        
        return res if res >= 2 else -1