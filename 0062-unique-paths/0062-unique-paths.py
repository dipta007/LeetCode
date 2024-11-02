class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tot_steps = m + n - 2
        one_side = m - 1

        def nCr(n, r):
            res = 1
            for i in range(r+1, n+1):
                res *= i
            for i in range(1, (n-r)+1):
                res //= i
            
            return res
        
        return nCr(tot_steps, one_side)
