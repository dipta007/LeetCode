class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0], -x[1]))

        p, b = [], []
        mx = 0
        p_done = {}
        for pp, bb in items:
            if pp not in p_done:
                p.append(pp)
                mx = max(mx, bb)
                b.append(mx)
                p_done[pp] = True
            
        res = []
        for q in queries:
            ind = bisect_right(p, q) - 1
            if ind < 0:
                res.append(0)
            else:
                res.append(b[ind])
        return res