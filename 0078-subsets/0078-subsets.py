class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def checkBit(x, n):
            return (1 << n) & x

        res = []
        for B in range(2 ** len(nums)):
            now = []
            for j in range(len(nums)):
                if checkBit(B, j):
                    now.append(nums[j])
            res.append(now)
        
        return res