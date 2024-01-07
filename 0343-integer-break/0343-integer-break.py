class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache
        def call(n):
            if n <= 1:
                return 1
            
            res = n
            for i in range(1, n):
                res = max(res, i * call(n - i))
            
            return res
        if n <= 3:
            return n-1
        return call(n)
