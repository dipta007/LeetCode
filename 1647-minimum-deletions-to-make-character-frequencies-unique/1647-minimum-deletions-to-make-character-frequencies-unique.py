class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import Counter
        mp = Counter(s)

        counters = Counter(mp.values())

        mark = {}
        res = 0
        for k in sorted(list(counters.keys())):
            v = counters[k]
            mark[k] = 1
            while v > 1:
                # print(k, v)
                for i in range(k, -1, -1):
                    # print(i, mark[i])
                    if i == 0 or i not in mark:
                        mark[i] = 1
                        break
                    res += 1
                v -= 1
        
        return res
        


        