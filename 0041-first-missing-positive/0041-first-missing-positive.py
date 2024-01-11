class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [x if x > 0 else 0 for x in nums]
        for i in range(len(nums)):
            v = abs(nums[i])
            if v == 0:
                continue
            elif v <= len(nums):
                v -= 1
                new_v = -(len(nums) + 4)
                if nums[v] < 0:
                    new_v = nums[v]
                if nums[v] > 0:
                    new_v = -nums[v]

                nums[v] = new_v
        
        for i in range(len(nums)):
            if nums[i] == 0 or nums[i] > 0:
                return i + 1
        
        return len(nums) + 1