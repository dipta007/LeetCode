class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0

        res = []
        while i < len(a) and j < len(b):
            s1, e1 = a[i]
            s2, e2 = b[j]

            if not (e2 < s1 or s2 > e1):
                s = max(s1, s2)
                e = min(e1, e2)
                res.append([s, e])
            
            if e1 < e2:
                i += 1
            else:
                j += 1
                

        return res