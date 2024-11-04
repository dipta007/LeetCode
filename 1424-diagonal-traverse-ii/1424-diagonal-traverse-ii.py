class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        grps = defaultdict(list)
        
        for r, row in enumerate(nums):
            for c, col in enumerate(row):
                d = r + c
                grps[d].append(row[c])

        res = []
        for k in grps.keys():
            g = grps[k]
            res.extend(reversed(g))
        return res