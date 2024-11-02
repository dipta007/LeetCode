class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        l, r = 0, len(nums) - 1
        pivot = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                pivot = m
                r = m - 1
            
        def search(l, r):
            res = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        
        # run 2 search
        lft = search(0, pivot-1)
        if lft == -1: return search(pivot, len(nums)-1)
        return lft