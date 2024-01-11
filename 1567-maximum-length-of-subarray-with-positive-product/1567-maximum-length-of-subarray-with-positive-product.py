# 0 1 -2 -3 -4 0 1 2 3 4 5
# 0 0 1 -2 -3 -4 0 1 2 3 4 5 0
# 1 1 1 -2 6 -24 1 1 2 6 24 120 1
#

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def get_max(l, r):
            if r < l:
                return 0

            print(l, r)

            if sum([1 if v < 0 else 0 for v in nums[l: r+1]]) % 2 == 0:
                return r - l + 1
            else:
                o1, o2 = -1, -1
                flg = 0
                for i in range(l, r + 1):
                    v = nums[i]
                    if v < 0 and o2 == -1:
                        o2 = i+1
                    if v < 0:
                        o1 = i-1
                return max(o1 - l + 1, r - o2 + 1)

        zero_inds = [i for i in range(len(nums)) if nums[i] == 0]
        zero_inds = [-1] + zero_inds + [len(nums)]

        res = 0
        for i in range(len(zero_inds) - 1):
            l = zero_inds[i]
            r = zero_inds[i+1]
            res = max(res, get_max(l+1, r-1))
        
        return res