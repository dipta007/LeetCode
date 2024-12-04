class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def call(curr, copy):
            if curr == n:
                return 0
            if curr > n:
                return 1000000
            
            res = 10000000
            if curr != copy:
                res = min(res, 1 + call(curr, curr))
            if copy:
                res = min(res, 1 + call(curr+copy, copy))

            return res
        
        return call(1, 0)