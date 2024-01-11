class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        mp = defaultdict(int)

        def update_with_divs(x, mp):
            xx = int(math.sqrt(x))
            for i in range(1, xx+1):
                if x % i == 0:
                    mp[i] += 1
                    if x // i != i:
                        mp[x // i] += 1

        res = 0
        for i, v in enumerate(nums):
            need = k // math.gcd(v, k)
            res += mp[need]

            update_with_divs(v, mp)
        
        return res