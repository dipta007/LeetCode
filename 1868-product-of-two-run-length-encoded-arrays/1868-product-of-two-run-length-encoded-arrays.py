class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        def prod(ar, br):
            res = []
            i, j = 0, 0
            while i < len(ar) and j < len(br):
                mn_f = min(ar[i][1], br[j][1])
                v = ar[i][0] * br[j][0]

                ar[i][1] -= mn_f
                br[j][1] -= mn_f

                if len(res) > 0 and res[-1][0] == v:
                    res[-1][1] += mn_f
                else:
                    res.append([v, mn_f])

                if ar[i][1] == 0: i += 1
                if br[j][1] == 0: j += 1
            return res

        return prod(encoded1, encoded2)
        