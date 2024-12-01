class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def check(arr):
            for a, b in zip(arr, arr[1:]):
                if a >= b:
                    return False
            return True

        for i in range(len(nums)-2*k+1):
            a = i
            b = i + k
            if check(nums[i:i+k]) and check(nums[i+k:i+2*k]):
                return True

        return False