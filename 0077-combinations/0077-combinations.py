class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def call(i, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            if i > n:
                return
            
            call(i+1, curr + [i])
            call(i+1, curr)
        
        call(1, [])

        return res