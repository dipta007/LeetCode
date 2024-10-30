class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {}
        for i, o in enumerate(order):
            rank[o] = i
        
        s = list(s)
        s.sort(key=lambda x: rank.get(x, len(s)))
        return "".join(s)