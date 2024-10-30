class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_gap(s):
            gaps = []
            for p, c in zip(s, s[1:]):
                ix = ord(c) - ord(p)
                gaps.append(ix if ix > 0 else ix + 26)
            g = "_".join(str(g) for g in gaps)

            return g
        
        from collections import defaultdict
        mp = defaultdict(list)
        for s in strings:
            mp[get_gap(s)].append(s)
        
        # print(mp)
        res = []
        for k, v in mp.items():
            res.append(v)
        return res