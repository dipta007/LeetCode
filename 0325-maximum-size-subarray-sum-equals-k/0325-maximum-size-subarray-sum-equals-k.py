class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mp_cum = {}
        cum = 0
        mp_cum[0] = -1

        res = 0
        for i, v in enumerate(nums):
            cum += v
            need = cum - k

            if need in mp_cum:
                res = max(res, i - mp_cum[need])
            if cum not in mp_cum:
                mp_cum[cum] = i

        return res 