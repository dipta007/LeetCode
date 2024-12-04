class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = [i for i in range(len(points))]

        def find(x):
            if par[x] == x: return x
            par[x] = find(par[x])
            return par[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            par[px] = py

        import heapq
        h = []

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        res = 0
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if p1 == p2: continue

                d = distance(p1, p2)

                heapq.heappush(h, (d, i, j))

        tot = 0
        while h and tot < len(points) - 1:
            d, x, y = heapq.heappop(h)

            if find(x) != find(y):
                tot += 1
                res += d
                union(x, y)

        return res