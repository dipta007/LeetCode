class Solution:

    def __init__(self, nums: List[int]):
        from collections import defaultdict
        self.mp = defaultdict(list)
        for i, v in enumerate(nums):
            self.mp[v].append(i)

    def pick(self, target: int) -> int:
        values = self.mp[target]
        import random
        rnd_idx = random.randint(0, len(values)-1)
        return values[rnd_idx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)