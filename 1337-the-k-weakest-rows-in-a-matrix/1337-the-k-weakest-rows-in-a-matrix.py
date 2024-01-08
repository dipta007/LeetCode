class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [(sum(row), i) for i, row in enumerate(mat)]
        power.sort()
        return [x for (_, x) in power[:k]]