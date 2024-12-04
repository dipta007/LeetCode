class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            v = abs(nums[i])
            if v > len(nums):
                v -= len(nums)

            if nums[v-1] < -len(nums) or nums[v-1] > len(nums):
                res.append(v)
            else:
                nums[v-1] += len(nums)
        return res