class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        gc = gcd(n, k)

        def get_median(vals):
            if len(vals) % 2 == 1:
                return vals[len(vals) // 2]

            return (vals[len(vals) // 2] + vals[len(vals) // 2 - 1]) // 2

        res = 0
        for i in range(gc):
            vals = []
            for j in range(i, n, gc):
                vals.append(arr[j])

            vals.sort()
            mm = get_median(vals)

            for v in vals:
                res += abs(mm - v)
        return res
