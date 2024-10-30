class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        lft = bisect.bisect_left(nums, target)
        rgt = bisect.bisect_right(nums, target)

        return [lft, rgt-1] if lft < len(nums) and nums[lft] == target else [-1, -1]