class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        arr_indices = defaultdict(set)

        print("1")

        mn, mx = int(4e5), -int(4e5)
        for i, num in enumerate(nums):
            for v in num:
                arr_indices[v].add(i)
                mn = min(mn, v)
                mx = max(mx, v)

        l = mn
        count = defaultdict(int)
        s = set()
        res = [mn, mx]
        for h in range(mn, mx+1):
            for v in arr_indices[h]:
                s.add(v)
                count[v] += 1

            while len(s) == len(nums):
                if h - l + 1 < res[1] - res[0] + 1:
                    res = [l, h]
                for v in arr_indices[l]:
                    count[v] -= 1
                    if count[v] == 0:
                        s.remove(v)
                l += 1

        return res