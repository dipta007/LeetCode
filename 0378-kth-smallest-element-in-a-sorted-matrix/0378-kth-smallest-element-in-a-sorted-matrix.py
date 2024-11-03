class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        h = []

        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            heapq.heappush(h, (matrix[i][0], i, 0))

        rem = k
        while True:
            v, rr, cc = heapq.heappop(h)
            rem -= 1
            if rem == 0:
                return v

            cc += 1
            if cc < c:
                heapq.heappush(h, (matrix[rr][cc], rr, cc))