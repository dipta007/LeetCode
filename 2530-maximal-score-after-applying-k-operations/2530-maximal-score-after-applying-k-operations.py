class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        h = []

        for v in nums:
            heapq.heappush(h, -v)

        res = 0
        while k:
            k -= 1
            v = -heapq.heappop(h)
            res += v
            heapq.heappush(h, -math.ceil(v / 3))
        
        return res