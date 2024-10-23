class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_ele = min(nums)
        max_ele = max(nums)

        count = [0] * (max_ele - min_ele + 4)
        for v in nums:
            count[v - min_ele] += 1
        
        for v in range(len(count)-1, -1, -1):
            k -= count[v]
            if k <= 0:
                return v + min_ele