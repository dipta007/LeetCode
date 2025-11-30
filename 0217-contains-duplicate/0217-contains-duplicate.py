class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n in count:
                return True
            count[n] = 1
        return False
        