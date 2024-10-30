class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anag = defaultdict(list)
        def call(s):
            return "".join(sorted(list(s)))

        for s in strs:
            anag[call(s)].append(s)

        return list(anag.values())