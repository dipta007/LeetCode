class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        for i in range(0, len(nums)): 
            curr = nums[i]
            if curr in last:
                lind = last[curr]
                if i - lind <= k:
                    return True
            last[curr] = i
        return False