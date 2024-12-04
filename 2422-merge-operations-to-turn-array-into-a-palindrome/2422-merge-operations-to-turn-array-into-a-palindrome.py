class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        res = 0
        while l <= r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            elif l + 1 == r:
                res += 1
                break
            elif nums[l] < nums[r]:
                nums[l+1] += nums[l]
                res += 1
                l += 1
            elif nums[r] < nums[l]:
                nums[r-1] += nums[r]
                res += 1
                r -= 1
        return res