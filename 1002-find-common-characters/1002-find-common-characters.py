class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        common = Counter(words[0])
        for w in words[1:]:
            count = Counter(w)

            nw = {}
            for k, v in count.items():
                if k in common:
                    nw[k] = min(v, common[k])

            common = nw
        
        res = []
        for k, v in common.items():
            while v:
                res.append(k)
                v -= 1
        return res
