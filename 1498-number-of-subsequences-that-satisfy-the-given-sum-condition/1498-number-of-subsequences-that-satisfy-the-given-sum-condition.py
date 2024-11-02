class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = int(1e9+7)
        res = 0
        nums.sort()
        for i, mn in enumerate(nums):
            if mn + mn > target:
                break

            l, h = i, len(nums) - 1
            mx_ind = i
            while l <= h:
                m = (l + h) // 2

                if mn + nums[m] <= target:
                    mx_ind = m
                    l = m + 1
                else:
                    h = m - 1
            
            sz = mx_ind - i + 1

            res += (2 ** (sz-1)) % MOD
        
        return res % MOD