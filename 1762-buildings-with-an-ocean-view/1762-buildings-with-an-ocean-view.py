class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        mx = 0
        for i, h in enumerate(heights[::-1]):
            if h > mx:
                mx = h
                res.append(len(heights) - i - 1)

        return sorted(res)