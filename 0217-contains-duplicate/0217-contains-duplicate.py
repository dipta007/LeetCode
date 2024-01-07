class Solution:
    def containsDuplicate(self, x: List[int]) -> bool:
        return len(set(x)) != len(x)
