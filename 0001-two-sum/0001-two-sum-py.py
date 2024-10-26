class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            v = nums[i]
            need = target - v
            if need in index:
                return [index[need], i]
            index[v] = i

            