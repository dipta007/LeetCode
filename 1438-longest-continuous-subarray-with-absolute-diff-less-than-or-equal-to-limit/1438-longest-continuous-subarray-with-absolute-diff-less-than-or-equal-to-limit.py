class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        import heapq
        from collections import defaultdict
        min_h = []
        max_h = []
        min_cnt = defaultdict(int)
        max_cnt = defaultdict(int)

        l = 0
        res = 0
        for h in range(len(nums)):
            hv = nums[h]
            heapq.heappush(min_h, hv)
            heapq.heappush(max_h, -hv)
            min_cnt[hv] += 1
            max_cnt[hv] += 1

            mn = min_h[0]
            mx = -max_h[0]
            
            # print(min_h, max_h)
            while mx - mn > limit:
                lv = nums[l]
                min_cnt[lv] -= 1
                max_cnt[lv] -= 1
                while min_cnt[min_h[0]] == 0:
                    heapq.heappop(min_h)
                
                while max_cnt[-max_h[0]] == 0:
                    heapq.heappop(max_h)
                
                mn = min_h[0]
                mx = -max_h[0]

                l += 1

            res = max(res, h - l + 1)

        return res