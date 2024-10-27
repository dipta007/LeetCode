class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        last_seen = {}
        for i, v in enumerate(nums):
            last_seen[v] = i

        res = []
        i = 0
        while i < len(nums):
            a = nums[i]
            j = i + 1
            while(j < len(nums)):
                b = nums[j]
                need_c = 0 - a - b

                if need_c in last_seen and last_seen[need_c] > j:
                    curr = tuple(sorted([a, b, need_c]))
                    res.append(curr)
                
                while j < len(nums) - 1 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i = i + 1
            
            i += 1

        return list(set(res))