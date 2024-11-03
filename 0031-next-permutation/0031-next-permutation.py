class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                ind = i - 1
                break

        if ind == -1:
            nums.sort()
            return nums

        ind2 = -1
        for i in range(ind, len(nums)):
            if nums[i] > nums[ind]:
                ind2 = i
        
        nums[ind], nums[ind2] = nums[ind2], nums[ind]

        # print(nums, ind, ind2)
        i, j = ind+1, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums