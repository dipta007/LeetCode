class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def total(n):
            return (n * (n+1)) // 2

        def check(v):
            left = index + 1
            right = n - index

            left_total = total(v)
            if v > left:
                left_total -= total(v-left)
            else:
                left_total += (left - v)
            
            right_total = total(v)
            if v > right:
                right_total -= total(v-right)
            else:
                right_total += (right - v)
            
            tot = left_total + right_total - v
            return tot <= maxSum

        l, h = 1, maxSum
        res = 0
        while l <= h:
            m = (l + h) // 2
            if check(m):
                l = m + 1
                res = m
            else:
                h = m - 1
        
        return res