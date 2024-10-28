class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def call(rem, curr):
            if rem < 0:
                return
            if rem == 0:
                nonlocal res
                res.append(",".join(str(x) for x in sorted(curr[:])))
                return

            for v in candidates:
                call(rem-v, curr + [v])
            
        call(target, [])
        res = list(set(res))
        res = [x.split(",") for x in res]
        res = [[int(x) for x in xx] for xx in res]
        return res