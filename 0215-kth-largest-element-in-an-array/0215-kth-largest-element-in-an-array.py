class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [x + 10000 for x in nums]
        mark = [0 for _ in range(20004)]

        for v in nums:
            mark[v] += 1
        
        for i in range(20000, -1, -1):
            if mark[i] >= k:
                return i - 10000
            k -= mark[i]