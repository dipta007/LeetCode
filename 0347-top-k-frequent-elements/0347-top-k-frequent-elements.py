class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)

        for v in nums:
            counter[v] += 1

        val_count = [(v, c) for v, c in counter.items()]

        val_count.sort(key=lambda x: -x[1])
        print(counter.items())

        return [x[0] for x in val_count[:k]]