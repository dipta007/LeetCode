class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        vis = [0] * 20

        res = []
        def call(curr):
            if len(curr) == len(nums):
                nonlocal res
                res.append(curr)
                return

            for i in range(len(nums)):
                if vis[i] == 0:
                    vis[i] = 1
                    call(curr + [nums[i]])
                    vis[i] = 0
            
        call([])
        return res