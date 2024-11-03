class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict
        h = []

        counter = defaultdict(int)
        for i in range(min(k, len(nums))):
            heapq.heappush(h, -nums[i])
            counter[nums[i]] += 1
        
        res = []
        res.append(-h[0])
        for i in range(k, len(nums)):
            prev = nums[i-k]
            counter[prev] -= 1

            while h and counter[-h[0]] == 0:
                heapq.heappop(h)
            
            heapq.heappush(h, -nums[i])
            counter[nums[i]] += 1

            res.append(-h[0])

        return res

        