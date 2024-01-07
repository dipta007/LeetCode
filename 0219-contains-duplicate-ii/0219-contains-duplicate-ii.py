class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in mp:
                nw = i - mp[v]
                if nw <= k:
                    return True
            mp[v] = i
        return False