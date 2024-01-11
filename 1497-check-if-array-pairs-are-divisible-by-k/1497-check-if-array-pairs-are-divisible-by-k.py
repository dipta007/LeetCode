class Solution:
    def canArrange(self, arr: List[int], K: int) -> bool:
        def get_by_mod(v):
            return 
        from collections import defaultdict
        mp = defaultdict(int)
        for v in arr:
            v %= K
            mp[v] += 1

        print(mp)
        for k in mp.keys():
            if k == 0 and mp[k] % 2 == 1:
                return False
            elif k!=0 and mp[k] != mp[K-k]:
                return False
        return True