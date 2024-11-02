class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        import heapq
        from collections import defaultdict
        min_h = []
        max_h = []
        counter = defaultdict(int)

        l = 0
        res = 0
        for h in range(len(nums)):
            hv = nums[h]
            heapq.heappush(min_h, hv)
            heapq.heappush(max_h, -hv)
            counter[hv] += 1

            mn = min_h[0]
            mx = -max_h[0]
            
            # print(min_h, max_h)
            while mx - mn > limit:
                lv = nums[l]
                counter[lv] -= 1
                while counter[min_h[0]] == 0:
                    heapq.heappop(min_h)
                
                while counter[-max_h[0]] == 0:
                    heapq.heappop(max_h)
                
                mn = min_h[0]
                mx = -max_h[0]

                l += 1

            res = max(res, h - l + 1)

        return res