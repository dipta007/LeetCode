class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        res = []
        cum = 0
        dq = deque()
        tk = k
        k = 2 * k + 1
        for n in nums:
            dq.append(n)
            cum += n

            if len(dq) > k:
                x = dq.popleft()
                cum -= x
            
            if len(dq) == k:
                res.append(cum // k)

        if tk * 2 >= len(nums):
            return [-1] * len(nums)
        else:
            res = [-1] * tk + res + [-1] * tk

        return res