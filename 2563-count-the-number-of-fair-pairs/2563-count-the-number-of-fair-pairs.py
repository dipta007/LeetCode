class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        vs = []
        res = 0
        for v in nums:
            l = lower - v
            u = upper - v

            l = bisect_left(vs, l) - 1
            u = bisect_right(vs, u)

            vs.append(v)

            if l < u:
                res += (u - l - 1)

        return res