class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        counter = {x: 1 for x in nums}
        for i, n in enumerate(nums):
            cnt = 0
            x = n
            while x in counter and counter[x]:
                counter[x] = 0
                x = x * x
                cnt += 1
            # print(n, cnt)
            res = max(res, cnt)
        
        return res if res >= 2 else -1