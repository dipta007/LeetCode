class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        uni = list(set(nums))

        uni.sort(key=lambda x: -count[x])
        
        return uni[:k]