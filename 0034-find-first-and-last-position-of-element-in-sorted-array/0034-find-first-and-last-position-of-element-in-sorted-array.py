class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect

        lft = bisect.bisect_left(nums, target)
        rgt = bisect.bisect_right(nums, target)
        if lft == -1 or lft >= len(nums) or nums[lft] != target:
            return [-1, -1]
        return [lft, rgt-1]