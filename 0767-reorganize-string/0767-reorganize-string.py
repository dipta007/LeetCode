class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        h = []

        from collections import defaultdict
        cnt = defaultdict(int)

        for c in s:
            cnt[c] += 1
        
        for c, v in cnt.items():
            heapq.heappush(h, (-v, c))

        res = ""
        while len(h) > 1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)

            res += x[1]
            res += y[1]

            if -x[0] > 1:
                heapq.heappush(h, (-(-x[0]-1), x[1]))
            if -y[0] > 1:
                heapq.heappush(h, (-(-y[0]-1), y[1]))
        
        if len(h) == 0:
            return res
        
        if -h[0][0] > 1:
            return ""

        res += h[0][1]
        return res