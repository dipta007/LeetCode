class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        mp = Counter(nums)

        res = []
        while sum(mp.values()):
            now = []
            for k, v in mp.items():
                if v:
                    now.append(k)
                    mp[k] -= 1
            res.append(now)
        
        return res