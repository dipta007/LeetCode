# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        res = n
        while l <= h:
            m = (l + h) // 2
            if isBadVersion(m):
                res = m
                h = m-1
            else:
                l = m+1
        
        return res
        