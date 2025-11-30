class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def _find_pivot():
            l, h = 0, len(nums) - 1
            res = -1
            while l <= h:
                m = (l + h) // 2
                if nums[m] > nums[0]:
                    l = m + 1
                else:
                    res = m
                    h = m - 1

            return res
        
        p = _find_pivot()
        i1 = bisect.bisect_left(nums[:p], target)
        i2 = bisect.bisect_left(nums[p:], target) + p
        if i1 < len(nums) and nums[i1] == target:
            return i1
        if i2 < len(nums) and nums[i2] == target:
            return i2
        return -1



