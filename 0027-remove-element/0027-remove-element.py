class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
        
        return last+1