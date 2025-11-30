class Solution:

    def __init__(self, w: List[int]):
        cum = [0]
        for _w in w:
            cum.append(cum[-1] + _w)
        self.cum = cum
        self.l = 1
        self.h = cum[-1]

    def pickIndex(self) -> int:
        rn = random.randint(self.l, self.h)
        l, h = 0, len(self.cum) - 1
        res = -1
        while l <= h:
            m = (l+h)//2
            if rn <= self.cum[m]:
                h = m - 1
                res = m
            else:
                l = m + 1
        return res - 1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()