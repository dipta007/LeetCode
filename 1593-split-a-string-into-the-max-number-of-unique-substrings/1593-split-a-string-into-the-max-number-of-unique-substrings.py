class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        from collections import defaultdict
        res = 1
        
        def call(i, count):
            if i == len(s):
                nonlocal res
                res = max(res, sum(count.values()))
                return True
            
            curr = ""
            nw = False
            for j in range(i, len(s)):
                curr += s[j]
                if count[curr] == 0:
                    count[curr] = 1
                    nw = nw or call(j+1, count)
                    count[curr] = 0

        call(0, defaultdict(int))

        return res
                