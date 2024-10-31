class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            jump_to = i + nums[i]
            if jump_to >= last_pos:
                last_pos = i

        # print(dp)        
        return last_pos == 0