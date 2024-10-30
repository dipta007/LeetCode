class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lower = 1
        for v in arr:
            if v > lower:
                missing = v - lower
                if k <= missing:
                    return lower + k - 1
                k -= missing
            lower = v + 1
        
        return lower + k - 1
