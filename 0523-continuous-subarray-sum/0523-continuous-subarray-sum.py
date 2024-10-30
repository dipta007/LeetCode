class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cum = 0
        last_index = {0: -1}
        for i, v in enumerate(nums):
            cum += v
            cum %= k
            if cum not in last_index:
                last_index[cum] = i
            elif i - last_index[cum] > 1:
                return True

        return False
        