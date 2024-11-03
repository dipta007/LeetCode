class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        import bisect
        mp_set = {}
        for i, v in enumerate(nums):
            if v not in mp_set:
                mp_set[v] = i
            else:
                need = i - k
                if mp_set[v] >= need:
                    return True
            
            mp_set[v] = i

        return False